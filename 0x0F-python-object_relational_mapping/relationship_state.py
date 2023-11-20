#!/usr/bin/python3
"""
- Improve the file model_state.py, and save it as relationship_state.py
- In addition to previous requirements, the class attribute cities must
  represent a relationship with the class City.
  If the State object is deleted, all linked City objects must be automatically
  deleted.
  Also, the reference from a City object to his State should be named state.
- You must use the module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
     class definition of a State and an instance Base = declarative_base()
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete', backref='state')
