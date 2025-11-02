# Zero short prompting =>

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBnDu3erjUoRRV_Cz5Cdl0cr0yp8s7vZhQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero shot prompting :- Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only answer coding related questions, do not answer anything else. Your name is Chota-Don. If user ask something other than coding just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # system Prompt=>
        {
            "role" : "system",
            "content" : SYSTEM_PROMPT
        },
        {
            "role" : "user",
            "content" : "Hey, can you make a python program to print your name buddy? " 
        }
    ]
)

print(response.choices[0].message.content)


# Zero shot Prompting means giving model a direct task/question without any prior examples