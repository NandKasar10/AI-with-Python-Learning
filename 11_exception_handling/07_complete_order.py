class InvalidChaiError(Exception) : pass

def bill (flavour, cups) :
    menu = {"masala":20, "ginger" : 40}
     
    try :
        if flavour not in menu :
         raise InvalidChaiError("That chai is not available ... !!")
        if not isinstance(cups, int) :
           raise TypeError("Number of cups must be an Integer .. !!")
        total = menu[flavour] * cups
        print(f"Your Bill for {cups} cups of {flavour} Chai : rupees {total}")
    except Exception as e:
       print("Error : ",e)
    finally : 
       print("Thank you for visiting ChaiCode !!!")

bill("mint",2)
bill("masala","three")
bill("ginger",3)