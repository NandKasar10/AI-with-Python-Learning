# Integer 

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"total grams : {total_grams}") #17

remaining_tea = black_tea_grams - ginger_grams
print(f"remaining tea grams : {remaining_tea}")#11

milk_litres = 7
servings = 4

milk_per_serving = milk_litres/servings

print(f"MILK per serving : {milk_per_serving}")#1.75

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots

print(f"While tea bags per pot : {bags_per_pot}") #1

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup

print(f"Leftover cardamom pods : {leftover_pods}") #1

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor

print(f"Scaled falvour strength : {powerful_flavour}") #8

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves : {total_tea_leaves_harvested}")