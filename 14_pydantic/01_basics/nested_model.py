from typing import List, Optional
from pydantic import BaseModel

# pydantic model nested way one into another
class Address(BaseModel):
    street : str
    city: str
    postal_code : str


class User (BaseModel) :
    id : int
    name : str
    address : Address

address = Address(
    street = "123 something",
    city = "Rajnandgaon",
    postal_code = "491441"
)

user1 = User(
    id = 1,
    name = "Nand",
    address = address
)

user_data = {
    "id" : 1,
    "name" : "Nand",
    "address" : {
        "street" : "123 something",
        "city" : "Rajnandgaon",
        "postal_code" : "491441"  
    }
}


user2 = User(**user_data)

print(f"User 2 : {user2}")