from fastapi import FastAPI
from Router.user_routes import router as user_router

app = FastAPI(title="My_FastAPI_Experience", version="0.1.0")

# Include the router from User_routes.py
app.include_router(user_router, prefix="/user", tags=["User"])
