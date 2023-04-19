#!/bin/env python3
"""creates a db model to manage all board columns"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column, ForeignKey
from sqlalchemy.orm import relationship


class Item(baseMod, Base):
    """create an instance of the item class"""
    __tablename__ = 'items'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)
    board_id = Column(String(64), ForeignKey('board.id'), nullable=False)
    board = relationship('Board', backref='items')

    def __init__(self, name, board_id, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name
        self.board_id = board_id
