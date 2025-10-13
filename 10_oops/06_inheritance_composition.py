class BaseChai :
    def __init__(self, type_,):
        self.type = type_

    def prepare(self) :
        print(f"Preparing {self.type} Chai .... !")

    
class MasalaChai (BaseChai) :
    def add_spices (self) :
        print("Adding Cardamom, Ginger and Cloves .... !")


class ChaiShop : 
    chai_cls = BaseChai
    # not inheriting basechai calss but only taking its reference
    # chai_cls variable has reference of BaseChai
    # when you are trying to inherit all the properties of some other class then you need not to like <class_name>() inside a class => syntax of composition

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self) :
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop) :
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()

fancy.chai.add_spices()