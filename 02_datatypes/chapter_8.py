# LIST (in other lang known as array)
# mutable

ingredients = ["water","milk","black tea"]

ingredients.append("sugar")

print(f"Ingredients are : {ingredients}")

ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

spice_options = ["ginger","milk"]
chai_ingredients = ["water", "sugar"]

chai_ingredients.extend(spice_options)
print(f"Chai : {chai_ingredients}")

#also has indexing starting from 0

chai_ingredients.insert(1,"tea leaves")
print(f"Chai : {chai_ingredients}")

last_added = chai_ingredients.pop()

print(f"Deleted value : {last_added}")

chai_ingredients.reverse()

print(f"Chai : {chai_ingredients}")

chai_ingredients.sort()

print(f"Chai : {chai_ingredients}")

sugar_level = [1,2,3,4,5]
print(f"Maximum Sugar Level : {max(sugar_level)}")
print(f"Minimum Sugar Level : {min(sugar_level)}")

# What is operator overloading ?
# => when an operator is used for doing more than one task that is  operator overloading.

base_liquid = ["water ","milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour

print(f"Liquid Mix : {full_liquid_mix}")

strong_brew = ["Black tea", "Water"]*3

print(f"Strong Brew :{strong_brew}")

# from operator import itemgetter

raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinn",b"Card")
print(f"Raw Spice Data : {raw_spice_data}")