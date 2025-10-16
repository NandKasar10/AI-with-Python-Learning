from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel) :
    username : str

    #at the end of the class =>
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters ..!!!")
        return v
    

class SignupData(BaseModel) :
    password : str
    confirm_password : str


    @model_validator(mode='after')
    def password_match(cls, value) :
        if value.password != value.confirm_password :
            raise ValueError("Password Do not match .. !!")
        return value