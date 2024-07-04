from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")

userRouter = APIRouter()
certificateRouter = APIRouter()
associationRouter = APIRouter()
loginRouter = APIRouter()