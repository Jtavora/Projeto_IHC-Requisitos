from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import UserController
from .CommonRouter import userRouter
from fastapi import Depends

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

@userRouter.get("/get_certificates/{user_id}", response_model=list[CertificateResponse])
def get_all_certificates(user_id: str):
    certificates = user_controller.get_user_certificates(user_id)
    return [certificate.to_dict() for certificate in certificates]

@userRouter.get("/get_all_users")
def get_all_users():
    return user_controller.get_all_users()

