# chai = "Ginger Chai"

# def prepare_chai(order) :
#     print("Preparing ", order)

# prepare_chai(chai)

chai = [1, 2, 3] # mutable means can change

def edit_chai(cup) :
    cup[1] = 42

edit_chai(chai)

print(chai)

def make_chai(tea, milk, sugar) :
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")
make_chai(tea="Green", sugar="Medium", milk="Yes")


def special_chai(*ingredients, **extras) :
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon","Cardmom", sweetener = "Honey", foam="yes")

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)


def chai_order(order = None):
    if order is None :
        order = []

chai_order()
chai_order()