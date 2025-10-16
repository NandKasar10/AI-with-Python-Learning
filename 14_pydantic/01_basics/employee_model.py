from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel) :
    id : int
    name : str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        description = "Employee Name",
        examples = "Nand Kumar Kasar"
    )
    department : Optional[str] = "General"
    salary : float = Field(
        ...,
        ge = 10000,
        le = 100000,
        description = "Annual Salary in usd"
    )

    class User(BaseModel) : 
        email : str = Field(
            ...,
            # regex = r''
            pattern = ""
        )
        phone : str = Field(..., pattern = "")
        age : int = Field(
            ...,
            ge=0,
            le = 150,
            description = "Age in years"
        )
        discount : float = Field(
            ...,
            ge = 0,
            le = 100,
            description = "Discount Percentage !!"
        )