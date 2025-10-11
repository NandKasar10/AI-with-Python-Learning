# STRINGS
# immutable

chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please ! ")

chai_description = "Aromatic and Bold"
#indexing starts from 0 and goes n-1 (n=actual size)
print(f"Full word : {chai_description[:]}")

print(f"First word : {chai_description[:8]}")

#<string_name>[starting_index:ending_index:step(gap,jump)]

print(f"Last word : {chai_description[12:]}")

#NOTE :- reversing a string can be done by [::-1]

print(f"reverse chai_description : {chai_description[::-1]}")


label_text = "Chai Speciãl"
encoded_label = label_text.encode("utf-8")
print(f"label_text : {label_text}")
print(f"encoded_label : {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"decoded_label : {decoded_label}")