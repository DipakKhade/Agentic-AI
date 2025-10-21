# Chain Of Thought Prompting   

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

    Hey you are a expert AI agent that solve maths problems.

    Rules:
    - you have to plan the things using chain of Thought
    - given some input you have to give the output in a json format
    - json format : {"step":"START"| "PLAN"|"OUTPUT", "content":"string"}


    Examples:
    Q: hey what is 2 + 3
    A:  {"step":"START", "content":"user want to add up the numbers 2 and 3"}
        {"step":"PLAN", "content":"if i add the 2 and 3 then the output become 5"}
        {"step":"OUTPUT", "content":"5"}
   
   if you dont have start in input then you can give the start json,
   if you have plan in input then you can give the next plan or the output 
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
            "content": "what is (a+b)^2"
        },
        {
            "role": "assistant",
            "content": json.dumps({"step":"START", "content":"The user wants to expand the algebraic expression (a+b)^2."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "I need to apply the formula for squaring a binomial, which is (x+y)^2 = x^2 + 2xy + y^2. In this case, x=a and y=b. So, (a+b)^2 = a^2 + 2ab + b^2."})
        },
    ]
)

print((response.choices[0].message))