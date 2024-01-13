#!/usr/bin/python3
'''
    A simple module since it has two classes (State, Base).
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    '''A simple class that declare a new state.'''

    __tablename__ = "states"
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref=backref("state", cascade="all"),
                          single_parent=True)
