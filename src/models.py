import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)






class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water =  Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)





class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)



class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    nickname = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)



class Favorite (Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('character'))
    starships_id = Column(Integer, ForeignKey('starships'))















    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')