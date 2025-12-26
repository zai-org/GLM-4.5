import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer(model_path, device="auto", dtype=torch.bfloat16):
    """
    Loads the GLM model and tokenizer from the specified path.
    """
    print(f"Loading model from {model_path}...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=model_path,
        torch_dtype=dtype,
        device_map=device,
        trust_remote_code=True
    )
    return model, tokenizer

def apply_template(tokenizer, messages, add_generation_prompt=True):
    """
    Applies the chat template to the provided messages.
    """
    return tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=add_generation_prompt,
        return_dict=True,
        return_tensors="pt",
    )
