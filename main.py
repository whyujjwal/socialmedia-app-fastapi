from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
class Post(BaseModel):
    title: str
    discription: str
    intger: int = 3


@app.get("/")
async def hello():
    return {"message":"hello world"}


@app.post("/post")
def create_post(data: Post):
    print(data)
    return {"message":"successfully created"}