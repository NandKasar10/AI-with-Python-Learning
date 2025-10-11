# x = 5 is a statement it will not return anything
# where 3+3 is an expression which returns something

# walrus operator => " := "

value = 13
# remainder = value % 5
if (remainder := value % 5) :
    print(f"Not Divisible, Remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your chai cup : ")) in available_sizes :
    print(f"Serving {requested_size} Chai!") 
else :
    print(f"Size is unavailable- {requested_size}")

flavours = ["masala", "lemon", "ginger", "mint"]

print(f"Available flavours : {flavours}")

while (flavour := input("Choose your flavour : ")) not in flavours :
    print(f"Sorry, {flavour} is not available!")

print(f"You choose {flavour} Chai, Serving in a minute !")