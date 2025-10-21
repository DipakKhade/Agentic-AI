# zero shot prompting, directly giving instructions to the model

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """hey you are the maths ai agent and ans only the queris realted to maths and in other case say sorry"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": ""
        }
    ]
)

print(response.choices[0].message)