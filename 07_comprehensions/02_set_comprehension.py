favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chais = {chai for chai in favourite_chais}

print(f"Unique Chais are : {unique_chais}")

recipes = {
    "Masala Chai" : ["ginger","cardmom","clove"],
    "Elaichi Chai" : ["cardmom","milk"],
    "Spicy Chai" : ["ginger","black pepper","clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}


print(f"Unique Spices are : {unique_spices}")