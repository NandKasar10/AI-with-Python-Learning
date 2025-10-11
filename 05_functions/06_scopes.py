def serve_chai() :
    chai_type = "Masala" #local scope
    print(f"Inside funcion {chai_type}")


chai_type = "Lemon" #global scope
serve_chai()
print(f"Outside function : {chai_type}")

def chai_counter() :
    chai_order = "lemon" #enclosing scope

    def print_order():
        chai_order = "Ginger"
        print(f"Inner : {chai_order}")
    print_order()
    print(f"Outer : {chai_order}")

chai_counter()