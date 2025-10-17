from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel) :
    street : str
    city : str
    zip_code : str

class User(BaseModel) :
    id : int
    name : str
    email : str
    is_active : bool = True
    createdAt : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime : lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    # json string wale mai date ache se aayega iske karan jiska use ho sakta hai

user = User(

    id = 1,
    name = "Nand",
    email = "example@abc",
    createdAt = datetime.now(),
    address= Address(
        street="Something",
        city = "Rajnandgaon",
        zip_code = "491441"
    ),
    is_active= False,
    tags= ["premium","subscriber"]

)

print(f"User : {user}")
print("=-="*30)

python_dict = user.model_dump()

print(f"python_dict  : {python_dict}")
print("=.="*30)

json_str = user.model_dump_json()

print(f"json_str  : {json_str}")