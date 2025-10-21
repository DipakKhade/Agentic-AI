# few shot prompting, directly giving instructions to the model with some examples

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    hey you are the maths ai agent and ans only the queris realted to maths and in other case say sorry

    Exapmles:
    question: tell me a story
    ans: hey sorry, i am a maths ai agent only able to answer the maths related questions

    question: what is 0!
    ans: the 0! is 1
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            # "content": "who is the prime minister of india"
            "content": "what is (a+b)^2"
        }
    ]
)

print(response.choices[0].message)