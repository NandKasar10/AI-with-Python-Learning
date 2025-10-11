def make_chai() :
    # return "Here is your Chai !"
    print( "Here is your Chai !")


return_value = make_chai()

print(return_value) # None

def idle_chaiwala() :
    pass

print(idle_chaiwala()) # None

def sold_cups () :
    return 120

total = sold_cups()
print(total) 


def chai_status(cups_left) :
    if cups_left == 0 :
        return "Sorry, Chai is Over"
    return "Chai is ready !"

print(chai_status(0))
print(chai_status(5))


def chai_report() :
    return 100, 20, 30 # sold, remaining

sold, remaining, _ = chai_report()
print("Sold : ", sold, " Remaining : ", remaining)