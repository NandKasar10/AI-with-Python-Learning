print("Start of pydantic journey ")

# PYDANTIC used for data validation and setting management

#use cases :-
# Data parsing and validation
# API development
# config management
# Data serilization / deserilization

from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {'id': 101, 'name' : "Chaicode", 'is_active' : 25}

user = User(**input_data) #**<dict_name> this unpacks dictionary

print(user)