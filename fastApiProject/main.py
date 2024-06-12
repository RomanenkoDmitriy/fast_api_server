from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from fastapi import Body, Request

from models import PhoneNumber
from engine import engine

app = FastAPI()
Session = sessionmaker(bind=engine)


class Item(BaseModel):
    hashed_phone_number: str
    phone_number: str


class ItemGet(BaseModel):
    hashed_phone_number: str


@app.get("/items/")
async def root(hashed_phone_number: str):
    with Session() as session:
        phone_numbers = session.query(PhoneNumber).get(hashed_phone_number)
        if phone_numbers:
            data = {'phone_numbers': phone_numbers.phone_number}
        else:
            data = {'phone_numbers': ''}
        return data


@app.post("/create_num/")
async def create_num(data: Item):
    print(data)

    phone_number = PhoneNumber(hash_number=data.hashed_phone_number, phone_number=data.phone_number)
    with Session() as session:
        session.add(phone_number)
        session.commit()
