#booleans

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling #upcasting #6

milk_present = 0 #no milk
print(f"Is there milk? {bool(milk_present)}")

# some falsy values : 0, "", None

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can Serve Chai? {can_server}")