# cot => chain of thought property

from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI(
    api_key="AIzaSyBnDu3erjUoRRV_Cz5Cdl0cr0yp8s7vZhQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few shot prompting :- Directly giving the instructions to the model and few examples to the model
SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules :
    - Strictly follow the given JSON OUTPUT format
    - Only run one step at a time
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

    Output JSON format : 
    {
    "step" : "START"|"PLAN"|"OUPUT",
    "content" : "string"
    }

    Example : 
    {
    "START" : "Hey, Can you solve 2 + 3 * 5 / 10",
    "PLAN" : "Seems like user is interested in math problem",
    "PLAN" : "looking at the problem, we should solve this problem using BODMAS method",
    "PLAN" : "Yes, The BODMAS is correct thing to be done here",
    "PLAN" : "first we must multiply 3 * 5 which is 15",
    "PLAN" : "Now the new equation is 2 + 15 / 10",
    "PLAN" : "Now we must perform division that is 15 / 10 which is 1.5",
    "PLAN" : "Now the new equation is 2 + 1.5",
    "PLAN" : "Finally lets perform addition that is 2 + 1.5 which is 3.5",
    "PLAN" : "Great, we have solved and finally have an answer as 3.5",
    "OUTPUT" : "3.5"
    }
"""
print("\n\n\n\n\n")

message_history = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
]

user_query = input("Enter anything 👉 ")

message_history.append({"role" : "user", "content" : user_query})

while True : 
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type" : "json_object"},
        messages= message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role" : "assistant", "content" : raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥 Started :- ",parsed_result.get("content"))
        continue

    elif parsed_result.get("step") == "PLAN" :
        print("🧠 Thinking :- ",parsed_result.get("content"))
        continue
    
    else :
        print("📬 Done :- ",parsed_result.get("content"))
        break


print("\n\n\n\n\n")
