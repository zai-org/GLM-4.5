import torch
import argparse
import sys
from utils import load_model_and_tokenizer, apply_template

def parse_args():
    parser = argparse.ArgumentParser(description="GLM-4.x Inference CLI")
    parser.add_argument("--model_path", type=str, default="zai-org/GLM-4.7", help="Path to the model")
    parser.add_argument("--max_new_tokens", type=int, default=512, help="Maximum new tokens to generate")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--top_p", type=float, default=0.9, help="Sampling top_p")
    parser.add_argument("--device", type=str, default="auto", help="Device to use (auto, cuda, cpu)")
    parser.add_argument("--thinking", action="store_true", help="Enable thinking mode")
    return parser.parse_args()

def main():
    args = parse_args()

    model, tokenizer = load_model_and_tokenizer(args.model_path, device=args.device)
    
    print("\nGLM-4.x Interactive Chat (type 'exit' to quit, 'clear' to reset history)")
    
    messages = []
    
    while True:
        try:
            user_input = input("\nUser: ").strip()
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                break
            if user_input.lower() == 'clear':
                messages = []
                print("Chat history cleared.")
                continue

            messages.append({"role": "user", "content": user_input})

            inputs = apply_template(tokenizer, messages)
            inputs = inputs.to(model.device)

            generate_kwargs = {
                "input_ids": inputs.input_ids,
                "attention_mask": inputs.attention_mask,
                "max_new_tokens": args.max_new_tokens,
                "do_sample": args.temperature > 0,
            }
            if args.temperature > 0:
                generate_kwargs["temperature"] = args.temperature
                generate_kwargs["top_p"] = args.top_p

            with torch.no_grad():
                generated_ids = model.generate(**generate_kwargs)

            # Support skipping the prompt in output
            input_length = inputs.input_ids.shape[1]
            response_ids = generated_ids[0][input_length:]
            response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
            
            print(f"\nAssistant: {response_text}")
            messages.append({"role": "assistant", "content": response_text})

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
