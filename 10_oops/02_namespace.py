# Each object that have been constructed using a class is poses some different properties but are not overlapping others properties

# and all the objects has its own entity which is called its NAMESPACE 

#toh basically namespace ka meaning hai ki agar kuch class se do teen object banaya hai aur usme kuch property add kiya yaa uska value alter kiya toh baaki object and classes mai farak nhi padta issiko ko namespace bolte hai alg alg hai sabka


class Chai :
    origin = "India" #properties / attributes


print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

#creating object from class chai

masala = Chai()

print("Masala : ",masala.origin)
print("Hot or not :",masala.is_hot)

masala.is_hot = False

print(f"CLass : {Chai.is_hot}")
print(f"Masala Object : {masala.is_hot}")

masala.flavour = "Masala"

print(f"MASALA FLAVOUR : {masala.flavour}")