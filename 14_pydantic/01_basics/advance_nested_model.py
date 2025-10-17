from pydantic import BaseModel
from typing import Optional, List, Union

# OPTIONAL NESTED MODELS
class Address(BaseModel) :
    street : str
    city  : str
    postal_code : str

class Company(BaseModel) :
    name : str
    address : Optional[Address] = None


class Employee(BaseModel) : 
    name : str
    company : Optional[Company] = None


#MIXED DATATYPES

class TextContent(BaseModel) :
    type : str = "text"
    content : str

class ImageContent(BaseModel):
    typr : str = "Image"
    url : str 
    alt_text : str

class Article(BaseModel) :
    title : str
    sections : List[Union[TextContent, ImageContent]]


# DEEPLY NESTED STRUCTURES
class Country(BaseModel) :
    name : str
    code : str

class State(BaseModel):
    name : str
    state: Country

class City(BaseModel):
    name : str
    state: State

class Address(BaseModel) :
    street : str
    city : City
    postal_code : str

class Organization(BaseModel) :
    name:str 
    head_quarter : Address
    branches  : List[Address]=[]