# MRO => Method Resolution Order
class A :
    label = "A : Base Class"

class B (A):
    label = "B : Masala Blend"

class C (A):
    label = "C : Herbal Blend"

class D (B,C):
    pass


cup = D()
print(cup.label)
print(D.__mro__)