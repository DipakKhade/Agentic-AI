import torch
from transformers import pipeline

pipeline = pipeline(task="text-generation", model="llama-3.1-8B-instruct", dtype=torch.bfloat16, device_map="auto")

chat = [
    {"role": "user", "content": "explain 0 factorial"}
]

response = pipeline(chat, max_new_tokens=512)

print(response[0]["generated_text"][-1]["content"])