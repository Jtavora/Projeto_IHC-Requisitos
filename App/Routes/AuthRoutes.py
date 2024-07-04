from .CommonRouter import loginRouter
from App.Auth import Auth
from fastapi import HTTPException
from App.Models.PydanticModels import *
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

auth = Auth()

@loginRouter.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = auth.user_login(form_data)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token