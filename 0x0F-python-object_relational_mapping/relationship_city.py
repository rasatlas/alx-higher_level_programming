#!/usr/bin/python3
"""
Improve the file model_city.py and save it as relationship_city.py
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
     class definition of a City
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
