#!/bin/env python3
"""model to create a board object"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column
from sqlalchemy.orm import relationship
from models import storage


class Board(baseMod, Base):
    """defines a board table"""
    __tablename__ = 'board'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)
    items = relationship('Item', backref='board')

    def __init__(self, name, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name


    @classmethod
    def get_board(self, id):
        """return a board based on it's id"""
        this_board = storage.get(Board, id)
        return this_board

    def 
