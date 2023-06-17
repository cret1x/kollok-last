from database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    addr = Column(String)
    price = Column(Integer)
    rating = Column(Float)
    description = Column(String)
    services = Column(String)

    def __init__(self, name, addr, price, rating, description, services):
        self.name = name
        self.addr = addr
        self.price = price
        self.rating = rating
        self.description = description
        self.services = services

    @property
    def base_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'addr': self.addr,
            'price': self.price,
            'rating': self.rating,
        }

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'addr': self.addr,
            'price': self.price,
            'rating': self.rating,
            'description': self.description,
            'services': self.services,
        }
    

    def __repr__(self):
        return "<Hotel('%s')>" % (self.name)


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer)
    in_date = Column(DateTime)
    out_date = Column(DateTime)

    def __init__(self, hotel_id, in_date, out_date):
        self.hotel_id = hotel_id
        self.in_date = in_date
        self.out_date = out_date

    @property
    def serialize(self):
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'in_date': self.in_date,
            'out_date': self.out_date,
        }

    def __repr__(self):
        return "<Booking('%d')>" % (self.hotel_id)


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer)
    rating = Column(Float)
    text = Column(String)

    def __init__(self, hotel_id, rating, text):
        self.hotel_id = hotel_id
        self.rating = rating
        self.text = text

    @property
    def serialize(self):
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'rating': self.rating,
            'text': self.text,
        }

    def __repr__(self):
        return "<User('%d')>" % (self.hotel_id)