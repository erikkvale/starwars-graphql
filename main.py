from fastapi import FastAPI
from database.models import Character

app = FastAPI()


@app.get("/")
async def get_character():
    return {"Hello": "Erik"}

