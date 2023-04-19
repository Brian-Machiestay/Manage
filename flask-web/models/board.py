#!/bin/env python3
"""model to create a board object"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column


class Board(baseMod, Base):
    """defines a board table"""
    __tablename__ = 'board'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)

    def __init__(self, name, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name
        
