from pydantic import BaseModel
#kuch datatype pydantic mai available hai aur jo nhi hai baaki typing se lelete hai
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str]
    #pydantic and typing mix => List[str]
    quantities : Dict[str, int]

class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None


cart_data = {
    "user_id" : 123,
    "items" : ["Laptop","Mouse","Keyboard"],
    "quantities" : {"laptop" : 1,"mouse":2,"keyboard":3},
}

cart = Cart(**cart_data)