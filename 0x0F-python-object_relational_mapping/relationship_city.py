#!/usr/bin/python3
'''
    A simple module since it has a one class (Table) `City`.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''
    A simple class that declare a new Table called `cities`.

    Class Attributes:
        - id (int)
        - name (string)
        - state_id (id)
    '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
