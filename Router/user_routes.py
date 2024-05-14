from fastapi import APIRouter, Query, Path 

from model.user_models import Item

router = APIRouter()

# @router.get("/")
# async def root(): 
#   return {"message": "Hello World"}


# @router.post("/")
# async def post():
#   return {"message": "Hello from the post route"}


# @router.put("/")
# async def put():
#   return {"message": "Hello from the put route"}


# @router.get("/users")
# async def list_users():
#   return {"message": "list user route"}


# @router.get("/users/me/")
# async def get_current_user():
#   return {"user_id": "the current user"}


# @router.get("/users/{user_id}")
# async def read_item(user_id: str):
#   return {"user_id": user_id} 


# @router.get("/foods{food_name}")
# async def get_food(food_name: FoodEnum):
#   if food_name == FoodEnum.vegetables:
#     return {"food_name": food_name, "message": "Vegetables are good for you"}
  
#   if food_name.value == "fruits":
#     return {"food_name": food_name, 
#             "message": "Fruits are good for you"}
  
#   return {"food_name": food_name, "message": "Dairy is good for you"}


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @router.get("/items")
# async def list_items(skip: int = 0 , limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @router.get("/items/{item_id}")
# async def get_items(item_id: str, q: str | None = None):
#   if q:
#     return {"item_id": item_id, "q": q}
#   return {"item_id": item_id}

 

# @router.post("/items")
# async def create_item(item: Item):
#   item_dict = item.dict()
#   if item.tax:
#     price_with_tax = item.price + item.tax
#     item_dict.update({"price_with_tax": price_with_tax})
#   return item_dict


# @router.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#   result = {"item_id": item_id, **item.dict()}
#   if q:
#     result.update({"q": q})
#   return result



# @router.get("/books")
# async def prob_items(q: str | None = Query(None, 
#                                            min_length= 3, 
#                                            max_length= 10, 
#                                            title= "sample query string",
#                                             description= "This is a sample query string",
#                                             deprecated=True,
#                                             alias= "item-query")):
  
  
#   results = {"books": [{"books_id": "Foo"}, {"books_id": "Bar"}]}
#   if q:
#     results.update({"q": q})
#   return results  


# @router.get("flag_validations/{flag_id}")
# async def show_flag_validations(
#   q: str = "Hello",
#   flag_id: int = Path(..., title= "The color of the flag to get", ge=10, le=100), 
#   size: float = Query(..., gt=0, lt=7.75)
# ):

#   results = {"flag_id": flag_id, "size": size}
#   if q:
#     results.update({"q": q})
#   return results


# part_7_multiple_body_parameter

@router.put("/items/{items_id}")
async def update_items(
  *,
  item_id: int = Path(..., title= "The ID of the item to get", ge=0, le=150),
  q: str | None = None,
  item: Item | None = None
):
  results = {"item_id": item_id}
  if q:
    results.update({q: q})
  if item:
    results.update({"item": item})
  return results
