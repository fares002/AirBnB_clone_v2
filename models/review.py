#!/usr/bin/python3
"""This is the review class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """This is the class for Review that contain the follwing
    Attributes:
        place_id: represent place id
        user_id: represent user id
        text: review description for the place
    """
    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
