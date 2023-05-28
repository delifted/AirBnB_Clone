#!/usr/bin/python3

from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int() 
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = []

