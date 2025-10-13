def serve_chai (flavour) :
    try:
        print(f"Preparing {flavour} Chai ....!")
        if (flavour == "unknown") :
            raise ValueError("We don't know that flavour !")
    except ValueError as e:
        print("Error : ",e)
    else :
        print(f"{flavour} chai is served !")
    finally : 
        print("Next Customer please .... !")

serve_chai("masala")
serve_chai("unknown")