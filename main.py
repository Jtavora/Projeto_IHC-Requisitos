from fastapi import FastAPI
from App.Routes import UserRoutes
from App.Routes import CertificateRoutes
from App.Models.CommonModel import Base, engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(UserRoutes.router, prefix="/users", tags=["users"])
app.include_router(CertificateRoutes.router, prefix="/certificates", tags=["certificates"])