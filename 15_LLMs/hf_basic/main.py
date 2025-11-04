from transformers import pipeline

pipe = pipeline("text-generation", model="google/gemma-2b")

messages = [
    {
        "role" : "user",
        "content" : [
            {"type" : "image", "url" : "https://resize.indiatvnews.com/en/resize/newbucket/1080_-/2023/04/rohit-ipl-trophy-2020-ipl-1-1682866640.jpg"},
            {"type" : "text", "text" : "Who is this person?"}
        ]
    }
]

pipe(text_inputs=messages)