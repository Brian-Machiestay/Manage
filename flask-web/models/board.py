#!/bin/env python3
"""model to create a board object"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column
from sqlalchemy.orm import relationship
import models


class Board(baseMod, Base):
    """defines a board table"""
    __tablename__ = 'board'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)
    items = relationship('Item', back_populates='board')

    def __init__(self, name, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name


    @classmethod
    def boards(cls):
        """return a board based on it's id"""
        this_board = models.storage.all(cls)
        return this_board

    @classmethod
    def board(cls, id):
        """return a single board based on the id"""
        bd = models.storage.one(cls, id)
        return bd
