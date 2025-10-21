from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

SYSTEM_PROMPT = """
You are an expert AI reasoning agent specialized in solving logical and mathematical problems.

Your task is to think step-by-step using a Chain of Thought (CoT) approach, but express your reasoning explicitly in structured JSON objects.

Each message you output must strictly follow this JSON schema:
{
  "step": "START" | "PLAN" | "OUTPUT",
  "content": "string"
}

Rules:
1. Always begin your reasoning with a `"START"` step explaining what the user is asking for or what needs to be solved.
2. Then, provide a `"PLAN"` step that describes your reasoning or the steps needed to reach the answer.
3. Finally, return the `"OUTPUT"` step containing the final answer.
4. Each response must contain **only one JSON object** (no extra commentary or text).
5. You may continue the reasoning process across multiple turns — START → PLAN → OUTPUT.
"""

user_input = input("hey how can I help you today? : ")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_input}
]

current_step = "START"

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )

    llm_raw = response.choices[0].message.content
    print(llm_raw)
    llm_res = json.loads(llm_raw)

    step = llm_res["step"]
    content = llm_res["content"]

    if step == "START":
        print("🧠 Thinking started...")
        current_step = "PLAN"
        message_history.append({"role": "assistant", "content": llm_raw})
        message_history.append({"role": "user", "content": "continue with your PLAN step."})

    elif step == "PLAN":
        print(f"📝 Plan: {content}")
        current_step = "OUTPUT"
        message_history.append({"role": "assistant", "content": llm_raw})
        message_history.append({"role": "user", "content": "now give the OUTPUT step."})

    elif step == "OUTPUT":
        print(f"✅ Final Answer: {content}")
        break

    else:
        print("⚠️ Unknown step, stopping.")
        break
