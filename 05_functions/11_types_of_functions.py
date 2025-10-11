# pure function =>
def pure_chai(cups) :
    return cups * 10

total_chai = 0 #global scope

#impure functions =>
# (not recommended)
def impure_chai(cups) :
    global total_chai
    total_chai += cups
    return total_chai

# Recursive functions =>

def pour_chai(n) :
    if n == 0 :
        return "All cups poured !"
    print( f"{n} Cups are left !")
    return pour_chai(n-1)

print(pour_chai(3))

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai : chai != "kadak", chai_types))

# lamda => anonymous functions

print(f" STRONG CHAI : {strong_chai}")