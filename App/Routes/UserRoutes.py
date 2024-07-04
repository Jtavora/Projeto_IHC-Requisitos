from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import UserController
from .CommonRouter import userRouter

user_controller = UserController()

@userRouter.post("/create_user", response_model=UserResponse)
def create_user(user: User):
    usuario = user_controller.create_user(user)
    if usuario:
        return usuario.to_dict()
    raise HTTPException(status_code=400, detail="User already exists")

@userRouter.get("/get_user_by_username/{username}", response_model=UserResponse)
def get_user_by_username(username: str):
    user = user_controller.get_user_by_username(username)
    if user:
        return user.to_dict()
    raise HTTPException(status_code=404, detail="User not found")

@userRouter.delete("/delete_user/{user_id}", response_model=UserResponse)
def delete_user(user_id: str):
    user = user_controller.delete_user(user_id)
    if user:
        return user.to_dict()
    raise HTTPException(status_code=404, detail="User not found")

@userRouter.put("/update_user/{user_name}", response_model=UserResponse)
def update_user(user_name: str, user: UserUpdate):
    updated_user = user_controller.update_user(user_name, user)
    if updated_user:
        return updated_user.to_dict()
    raise HTTPException(status_code=404, detail="User not found")
