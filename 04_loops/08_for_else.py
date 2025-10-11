staff = [("Amit",18), ("Zara", 17), ("Raj", 17), ("Simran", 21)]

for name, age in staff :
    if age>=18 :
        print(f"{name} is eligible to manage the staffs")
        break
else :
    print("No one is eligible to manage the staff")
