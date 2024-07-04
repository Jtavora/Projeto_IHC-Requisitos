from fastapi import FastAPI
from App.Routes import *
from App.Routes import associationRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(userRouter, prefix="/users", tags=["users"])
app.include_router(certificateRouter, prefix="/certificates", tags=["certificates"])
app.include_router(associationRouter, prefix="/associations", tags=["associations"])
app.include_router(loginRouter, tags=["login"])
