# Few short prompting =>

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBnDu3erjUoRRV_Cz5Cdl0cr0yp8s7vZhQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few shot prompting :- Directly giving the instructions to the model and few examples to the model
SYSTEM_PROMPT = """You should only and only answer coding related questions, do not answer anything else. Your name is Chota-Don. If user ask something other than coding just say sorry.

Rule :
- Strictly follow the output in JSON format

Output Format :
{{
"code" : string or NULL,
"isCodingQuestion" : boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{
"code" : NULL,
"isCodingQuestion" : false
}}

Q: Hey, Write a code in python for adding two numbers?
A: {{
"code" : "def add(a,b):
            return a+b ",
"isCodingQuestion" : true
}}
"""

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
            "content" : "Hey, can you explain me a + b while creating a function in python code?" 
        }
    ]
)

print(response.choices[0].message.content)


# In Few-shot-prompting :- The model is provided with a few examples before asking it to generate a response.