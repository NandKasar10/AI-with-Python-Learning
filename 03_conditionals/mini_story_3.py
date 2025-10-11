cup_size = input("Enter the size of the cup you want(small/medium/large) : ").lower()


if cup_size == "small" :
    print(f"The Total amount of {cup_size} cup will be : {10}")
elif cup_size == "medium" :
    print(f"The Total amount of {cup_size} cup will be : {15}")
elif cup_size == "large" :
    print(f"The Total amount of {cup_size} cup will be : {30}")
else :
    print("Unknown cup size. PLease check the input !")