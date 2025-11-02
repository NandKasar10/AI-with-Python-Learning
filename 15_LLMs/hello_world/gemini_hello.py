from google import genai

client = genai.Client(
    api_key="AIzaSyBnDu3erjUoRRV_Cz5Cdl0cr0yp8s7vZhQ"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's your name buddy? If not have one, then think of most closed resemblence name according to your job. "
)

print(response.text)