#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """this calss is for Amenity
    Atrributes:
        name: the name of the amenity
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('place', secondary=place_amenity)
