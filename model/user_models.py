from enum import Enum
from pydantic import BaseModel

# class FoodEnum(str, Enum):
#   fruits = "fruits"
#   vegetables = "vegetables"
#   dairy = "dairy"


# class Item(BaseModel):
#   name: str
#   description: str | None = None
#   price: float
#   tax: float | None = None

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None


# class User(BaseModel):
#   user_name: str
#   full_name: str | None = None