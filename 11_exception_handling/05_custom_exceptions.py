def brew_chai (flavour) :
    if flavour not in ["masala", "ginger", "elaichi"] :
        raise ValueError("Unsupported Chai flavour ..... !")
    print(f"Brewing {flavour} Chai !!!")


brew_chai("mint")