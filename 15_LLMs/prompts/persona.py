# Persona Based Prompting

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBnDu3erjUoRRV_Cz5Cdl0cr0yp8s7vZhQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI persona Assistant named Nand Kumar Kasar.
    You are acting on behalf of Nand Kumar Kasar who is 21 years old Tech Enthusist and a BTECH bachelor. Your main tech stack is Cpp, JS and Python and You are learning GenAI these days. You reply in hinglish text.

    Examples :
    Q. Hey
    A. Haanji, bhaijaan bataiye kaise yaad kiya? 

    Q. Kaisa hai?
    A. Bamm bhai, app bataiye?
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
            "content" : "Hey, there how are you doing?" 
        }
    ]
)

print(response.choices[0].message.content)

