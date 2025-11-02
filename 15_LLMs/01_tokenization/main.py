import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there, My name is Nand Kumar Kasar."

tokens = enc.encode(text)
print(f"encoded text tokens : {tokens}")
#  encoded text tokens : [25216, 1354, 11, 3673, 1308, 382, 478, 427, 70737, 31358, 277, 13]

decoded = enc.decode([25216, 1354, 11, 3673, 1308, 382, 478, 427, 70737, 31358, 277, 13])

print(f"decoded version of tokens will be : {decoded}")