chai_type = "Irani"
def update_order() :
    chai_type = "Elaichi"

    def kitchen() :
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update",chai_type)
update_order()
print("globally",chai_type)