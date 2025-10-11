order_amount = int(input("Please enter the total amount : "))
delivery_cost = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_cost}") 