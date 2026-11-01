"""Execute the README's tool example over the real SDK with offline HTTP."""

import contextlib
import io
import json
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx
from openai import OpenAI

EXAMPLE = Path(__file__).resolve().parents[1] / "inference" / "api_request.py"


def completion(message):
    return {
        "id": "completion-example",
        "object": "chat.completion",
        "created": 0,
        "model": "test-model",
        "choices": [{"index": 0, "message": message, "finish_reason": "stop"}],
    }


class ToolExampleTest(unittest.TestCase):
    def execute_example(self, calls, require_tools=True):
        requests = []

        def respond(request):
            payload = json.loads(request.content)
            requests.append(payload)
            if len(requests) == 1:
                if calls and (not require_tools or payload.get("tools")):
                    message = {
                        "role": "assistant",
                        "content": None,
                        "tool_calls": calls,
                    }
                else:
                    message = {"role": "assistant", "content": "No tool needed."}
                return httpx.Response(200, json=completion(message))
            return httpx.Response(
                200,
                json=completion({"role": "assistant", "content": "Weather received."}),
            )

        output = io.StringIO()
        with OpenAI(
            api_key="offline-key",
            base_url="https://example.com/v1",
            max_retries=0,
            http_client=httpx.Client(transport=httpx.MockTransport(respond)),
        ) as client:
            with (
                patch("openai.OpenAI", return_value=client),
                contextlib.redirect_stdout(output),
            ):
                runpy.run_path(str(EXAMPLE), run_name="__main__")
        return requests, output.getvalue()

    @staticmethod
    def calls(*locations):
        return [
            {
                "id": f"call-generated-{index}",
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "arguments": json.dumps({"location": location}, ensure_ascii=False),
                },
            }
            for index, location in enumerate(locations)
        ]

    def test_initial_request_advertises_weather_tool(self):
        requests, output = self.execute_example(self.calls("北京"))
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0]["tools"][0]["function"]["name"], "get_weather")
        self.assertIn("Weather received.", output)

    def test_tool_response_uses_returned_call_id(self):
        calls = self.calls("北京")
        requests, _ = self.execute_example(calls, require_tools=False)
        messages = requests[1]["messages"]
        self.assertEqual(messages[-1]["tool_call_id"], calls[0]["id"])
        self.assertEqual(json.loads(messages[-1]["content"])["location"], "北京")

    def test_all_returned_calls_receive_matching_results(self):
        calls = self.calls("北京", "Bogotá")
        requests, _ = self.execute_example(calls, require_tools=False)
        results = [m for m in requests[1]["messages"] if m["role"] == "tool"]
        self.assertEqual([m["tool_call_id"] for m in results], [c["id"] for c in calls])
        self.assertEqual(
            [json.loads(m["content"])["location"] for m in results], ["北京", "Bogotá"]
        )

    def test_normal_assistant_response_does_not_require_a_tool_call(self):
        requests, output = self.execute_example([])
        self.assertEqual(len(requests), 1)
        self.assertIn("No tool needed.", output)


if __name__ == "__main__":
    unittest.main()
