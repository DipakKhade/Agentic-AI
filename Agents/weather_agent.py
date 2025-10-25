from openai import OpenAI
import requests
import json
import time
import re



import json

def extract_json_objects(text: str):
    json_objects = []
    brace_stack = []
    start_index = None

    for i, ch in enumerate(text):
        if ch == '{':
            if not brace_stack:
                start_index = i
            brace_stack.append('{')
        elif ch == '}':
            if brace_stack:
                brace_stack.pop()
                if not brace_stack and start_index is not None:
                    snippet = text[start_index:i+1]
                    try:
                        obj = json.loads(snippet)
                        json_objects.append(obj)
                    except json.JSONDecodeError:
                        pass
                    start_index = None
    return json_objects



SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.
For every tool call, wait for the OBSERVE step which is the output from the called tool.

Rules:
- Strictly Follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (where user gives an input), PLAN (that can be multiple times), and finally OUTPUT.

Output JSON Format:
{ "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

Available Tools:
- get_weather(city: str): Takes city name as input string and returns weather info.

Example:
START: What is the weather of Delhi?
PLAN: { "step": "PLAN", "content": "Seems like user is interested in weather of Delhi." }
PLAN: { "step": "PLAN", "content": "We have get_weather tool available." }
PLAN: { "step": "TOOL", "tool": "get_weather", "input": "delhi" }
PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temp of delhi is cloudy with 20 C" }
OUTPUT: { "step": "OUTPUT", "content": "The current weather in delhi is cloudy with 20°C." }
"""

# --- Tools ---
def get_weather(city: str) -> str:
    response = requests.get(f"https://wttr.in/{city.lower()}?format=%C+%t")
    if response.status_code == 200:
        return response.text
    return "Something went wrong fetching weather info."

available_tools = {
    "get_weather": get_weather
}


client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

query = input("Ask me anything: ")
message_history.append({"role": "user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=message_history
    )

    llm_raw = response.choices[0].message.content
    print(llm_raw)
    # llm_res = json.loads(llm_raw)
    json_blocks = extract_json_objects(llm_raw)
    for llm_res in json_blocks:
        step = llm_res["step"]


    step = llm_res["step"]

    if step == "START":
        print("🧠 Thinking started...")
        message_history.append({"role": "assistant", "content": llm_raw})
        message_history.append({"role": "user", "content": "continue with your PLAN step."})
        continue

    elif step == "PLAN":
        print(f"📝 Plan: {llm_res['content']}")
        message_history.append({"role": "assistant", "content": llm_raw})
        message_history.append({"role": "user", "content": "continue planning or give final output."})
        continue

    elif step == "TOOL":
        tool_name = llm_res["tool"]
        tool_input = llm_res["input"]
        print(f"🔧 Calling tool '{tool_name}' with input: {tool_input}")
        tool_response = available_tools[tool_name](tool_input)
        print(f"🪄 Tool result: {tool_response}")
        message_history.append({
            "role": "assistant",
            "content": json.dumps({
                "step": "OBSERVE",
                "tool": tool_name,
                "output": tool_response
            })
        })
        message_history.append({"role": "user", "content": "continue planning with the observed result."})
        continue

    elif step == "OUTPUT":
        print(f"Final Answer: {llm_res['content']}")
        break

    else:
        print("Unknown step, stopping.")
        break
