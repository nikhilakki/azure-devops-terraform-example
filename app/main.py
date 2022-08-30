import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.fibbonaci import check_fibbo_num

api = FastAPI()


class FibboPayload(BaseModel):
    number: int


@api.get("/")
def hello():
    return {"response": "Health Check Success"}


@api.post("/fibbo")
def fibbonaci_check(fibboPayload: FibboPayload):
    number = fibboPayload.number
    response = check_fibbo_num(number)
    return {"number": number, "response": response}


if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)
