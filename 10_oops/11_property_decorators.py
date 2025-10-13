class TeaLeaf :

    def __init__(self, age):
        self._age = age
    
    @property
    def age(self) :
        return self._age + 2
    
    @age.setter
    def age(self, age) :
        if 1 <= age <= 5 :
            self_age = age
        else :
            raise ValueError("Tea leaf must be between 1 and 5 years of age")

leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 7
print(leaf.age)