from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "explain me what is 2+2 and why"
        }
    ]
)

print(response.choices[0].message)