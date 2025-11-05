from openai import OpenAI
import requests

client = OpenAI(
    api_key="AIzaSyDwgE2rGJ7CnrH5PVnplhRGtR32cDSgc2c",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def get_weather( city : str ):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200 :
        return f"The Weather in {city} is {response.text}"
    
    return "Something went wrong 😢!!"

def main():
    user_query = input("😃 >  ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role" : "user",
                "content" : user_query 
            }
        ]
    )

    print("🤖 : ",response.choices[0].message.content)


# main()
print(get_weather("rajnandgaon"))