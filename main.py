from fastapi import FastAPI
import App.Routes
import App.Models
from App.Routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router, prefix="/users", tags=["users"])
app.include_router(router, prefix="/certificates", tags=["certificates"])