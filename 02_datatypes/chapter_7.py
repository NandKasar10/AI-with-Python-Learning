#TUPLES ----> (~~~~)
# immutable

masala_spices = ("cardamom","clove","cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main Masala Spices : {spice1}, {spice2}, {spice3}")
# known as unpacking

ginger_ratio, cardamom_ratio = 2, 1
# this is valid and will work because in background python treats it as a tuple unpacking

print(f"Ratio of Ginger : {ginger_ratio} and Cardamom : {cardamom_ratio}")

#SWAPPING
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ratio of Ginger : {ginger_ratio} and Cardamom : {cardamom_ratio}")

# membership

print(f"Is Ginger in Masala Spices ? {'ginger' in masala_spices}")
print(f"Is Cinnamon in Masala Spices ? {'cinnamon' in masala_spices}")

# in keyword used with tuples

#COLLEGE WALA (Sonal Yadav):=>
#:=)

t1 = (1,2,3,4,5,6,7,8,9,10)
#t1 = ("a") =>type string
#t1 = ("a",.....) =>type tuple
print("tuple1 : ",t1)

print(f"tuple1 type: {type(t1)} ")

for item in t1 :
    print(f"elem : {item}")

new_list=[item for item in t1]
print(f"new_list  : {new_list}")