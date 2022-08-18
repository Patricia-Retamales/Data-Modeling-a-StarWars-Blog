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

class User(Base):
    __tablename__='user'
    id= Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Favoritos(Base):
    __tablename__='favoritos'
    id= Column(Integer, primary_key=True)
    seguidores= Column(String(250))
    seguidores_id=Column(Integer, ForeignKey('user.id'))

    class Personajes(Base):
    __tablename__='personajes'
    id= Column(Integer, primary_key=True)
    personajes= Column(String(250))
    personajes_id=Column(Integer, ForeignKey('user.id'))
    personajesfavorito_id=Column(Integer, ForeignKey('favoritos.id'))

class Detallaspersonajes(Base):
    __tablename__='Detallaspersonajes'
    id= Column(Integer, primary_key=True)
    detallespersonajes= Column(String(250))
    detallespersonajes_id=Column(Integer, ForeignKey('personajes.id'))

    class Planetas(Base):
    __tablename__='planetas'
    id= Column(Integer, primary_key=True)
    planetas= Column(String(250))
    clima= Column(String(250))
    planetas_id=Column(Integer, ForeignKey('user.id'))
    planetasfavorito_id=Column(Integer, ForeignKey('favoritos.id'))

class Tiposplanetas(Base):
    __tablename__='tiposplanetas'
    id= Column(Integer, primary_key=True)
    tiposplanetas= Column(String(250))
    tiposplanetas_id=Column(Integer, ForeignKey('planetas.id'))

    class Naves(Base):
    __tablename__='naves'
    id= Column(Integer, primary_key=True)
    nave= Column(String(250))
    nave_id=Column(Integer, ForeignKey('user.id'))
    navefavoritos_id=Column(Integer, ForeignKey('favoritos.id'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')