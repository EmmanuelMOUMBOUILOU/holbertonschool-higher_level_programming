#!/usr/bin/python3
"""Defines the City class linked to the MySQL table cities."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city in the database.

    Attributes:
        id (int): Primary key, unique city ID.
        name (str): Name of the city.
        state_id (int): Foreign key linking to states.id.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
