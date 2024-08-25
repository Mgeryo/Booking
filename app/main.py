from datetime import date
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    hotel_id: int
    location: str
    name: str
    stars: Optional[int] = None

@app.get("/hotels/{hotel_id}")
def main(
    hotel_id: int, 
    location: str,
    name: str,
    stars: Optional[int] = None,)-> list[SHotel]:
    return [{
        "hotel_id": hotel_id,
        "location": location,
        "name": name,
        "stars": stars,
    }]

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    price: int


@app.post("/bookings")
def booking(book: SBooking):
    pass
    