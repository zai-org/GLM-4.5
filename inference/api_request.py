import argparse
import json
import sys
from openai import OpenAI

def parse_args():
    parser = argparse.ArgumentParser(description="GLM-4.x API Request Tool")
    parser.add_argument("--api_key", type=str, default="EMPTY", help="OpenAI API key")
    parser.add_argument("--base_url", type=str, default="http://127.0.0.1:8000/v1", help="API base URL")
    parser.add_argument("--model", type=str, default="zai-org/GLM-4.7", help="Model name")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--no_thinking", action="store_true", help="Disable thinking mode")
    return parser.parse_args()

def main():
    args = parse_args()
    
    client = OpenAI(
        api_key=args.api_key,
        base_url=args.base_url,
    )

    print(f"GLM-4.x API Client (Model: {args.model})")
    print("Type 'exit' to quit.")

    messages = []
    
    while True:
        try:
            user_input = input("\nUser: ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                break

            messages.append({"role": "user", "content": user_input})

            extra_body = {}
            if args.no_thinking:
                extra_body["chat_template_kwargs"] = {"enable_thinking": False}

            response = client.chat.completions.create(
                model=args.model,
                messages=messages,
                temperature=args.temperature,
                extra_body=extra_body if extra_body else None
            )

            assistant_message = response.choices[0].message
            print(f"\nAssistant: {assistant_message.content}")
            messages.append(assistant_message)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
