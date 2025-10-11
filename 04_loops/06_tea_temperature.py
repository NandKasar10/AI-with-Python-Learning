temp = int(input("Enter any temperature you want : "))

if temp>=40 : 
    print(f"Temperature : {temp}")

while temp>=40 and temp<100 :
    temp += 15
    print(f"Temperature : {temp}")

if(temp>=100) :
    print("Tea is ready to served!")
else :
    print(f"Temprature : {temp}, needs to be boiled first!")