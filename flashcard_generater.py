from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from huggingface_hub import login
import os
from dotenv import load_dotenv
access_token = os.getenv("HF_ACCESS_TOKEN")  # Read from environment variable

load_dotenv()
# Login to Hugging Face (Enter token when prompted)
login(access_token)

# Model name
model_name = "meta-llama/Llama-2-7b-chat-hf"

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,  # float16 only works on GPUs, so use float32
    device_map=None,  # This prevents auto-assigning CUDA
    token=access_token
)

# Generate flashcard data
prompt = "Give me a vocabulary word, its definition, and an example sentence."
# inputs = tokenizer(prompt, return_tensors="pt").to("cuda")  # Change to "cpu" if no GPU
inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
output = model.generate(**inputs, max_length=100)
result = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Flashcards:")
print(result)
