# SETS ---> {~~~~}

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices

print(f"All Spices : {all_spices}")

common_spices = essential_spices & optional_spices

print(f"Common Spices : {common_spices}")

only_in_essential = essential_spices - optional_spices


print(f"Only in Essential Spices : {only_in_essential}")

print(f"Is Cloves in Essential Spices : {'cloves' in optional_spices}")