#!/usr/bin/python3
"""Defines the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the place.

    Attributes:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of the bathrooms.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): the ids of the amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
