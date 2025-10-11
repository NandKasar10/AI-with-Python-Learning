menu = ["Green","Lemon","Spiced","Mint"]

#enumerate means [(0,"Green"),(1,"Lemon") and so on....]

for idx, item in enumerate(menu, start=1) :
    print(f"{idx} : {item} Chai")