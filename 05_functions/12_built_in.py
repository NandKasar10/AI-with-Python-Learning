def chai_flavour( flavour = "masala") :
    """<RETURNS THE FLAVOUR OF CHAI>""" #it needs to be first line only
    
    chai = "Ginger"
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

# __ => called as dunder

def generate_bill( chai = 0, samosa = 0) :
    """
    Calculate the total bill for chai and samosa :
    params :- 
    *chai( no. of chai cups 10 rupees each)
    *samosa ( no. of samosa 15 rupees each)

    return => total amount, and a thank you message as string
    """

    total = chai * 10 + samosa * 15

    return total, "Thank you for visiting us"

print(generate_bill.__doc__)