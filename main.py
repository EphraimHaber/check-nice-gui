import frontend.frontend as frontend
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


frontend.init(app)
