menu = [
    "Masala Chai" ,
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

# list_comprehension_syntax => expression for item in iterable if condition

print(f"Iced Tea : {iced_tea}")