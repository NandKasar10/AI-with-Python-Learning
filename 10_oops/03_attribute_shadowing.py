class Chai : 
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print("Before in cutting : ",cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("After updating in cutting : ",cutting.temperature)
print("class structure : ",Chai.temperature)

del cutting.temperature

print("After deleting temp.  in cutting : ",cutting.temperature)

print("Before Cup size of cutting : ",cutting.cup  )

del cutting.cup

print("After deleting Cup size of cutting : ",cutting.cup  ) #error