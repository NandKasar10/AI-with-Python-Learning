# DICTIONARY

chai_order = dict(type="Masala Chai", size= "Large", sugar = 2 )
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai Recipe : {chai_recipe}")
print(f"Chai Recipe Base : {chai_recipe['base']}")

del chai_recipe["liquid"]
print(f"Chai Recipe : {chai_recipe}")

print(f"Is Sugar in the order ? {'sugar' in chai_order}")

chai_order = {"type" : "Ginger Chai", "size" : "Medium", "sugar" : 1}

print(f"Order details (keys) : {chai_order.keys()}")
print(f"Order details (values) : {chai_order.values()}")
print(f"Order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()

extra_spices = {"cardamom" : "crushed", "ginger" : "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe : {chai_recipe}")

customer_note = chai_order.get("note","NO NOTE AVAILABLE")
print(f"Customer Note : {customer_note}")
# used for showing a message if key not present to avoid crashes