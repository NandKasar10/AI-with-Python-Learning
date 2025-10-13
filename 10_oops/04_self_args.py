class Chaicup : 
    size = 150 # ml

    def describe (self) :
        return f"A {self.size} ml Chai cup !"
    

cup = Chaicup()
print(cup.describe())
# above one has the context of describe as it is an object based on class

print(Chaicup.describe(cup))
# this one does not have context as Chaicup is a class structure so we need to give the context here in the form of any object here used "cup"

