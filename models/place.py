#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'), primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True,
        nullable=False
    ),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps="place_amenities")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Get reviews function"""
            reviews_list = []
            for review in reviews_list:
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Get amenities function"""
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            """set linked Amenities"""
            if type(amenity) == Amenity:
                self.amenity_ids.append(amenity.id)
