from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

def add_numbers(a: int, b: int) -> int:
    return a + b

@app.post("/add")
def add_api(numbers: Numbers):
    result = add_numbers(numbers.a, numbers.b)
    return {"sum": result}


# uvicorn main:app --reload