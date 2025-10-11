import recipes.flavours

print("1 => ",recipes.flavours.elaichi_chai())

from recipes.flavours import   elaichi_chai,ginger_chai

print("2 => ",ginger_chai())

from .recipes.flavours import ginger_chai

