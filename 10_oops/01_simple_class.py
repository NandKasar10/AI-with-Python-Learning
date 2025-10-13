class Chai :
    pass

class ChaiTime :
    pass

# print(type(Chai)) => class type but we know everything is object in python so class is also an object


ginger_tea = Chai()

print(type(ginger_tea))

print(type(ginger_tea) is Chai)

print(type(ginger_tea) is ChaiTime)
