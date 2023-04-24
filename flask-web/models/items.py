#!/bin/env python3
"""creates a db model to manage all board columns"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column, ForeignKey
from sqlalchemy.orm import relationship
import models


class Item(baseMod, Base):
    """create an instance of the item class"""
    __tablename__ = 'items'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False)
    board_id = Column(String(64), ForeignKey('board.id'), nullable=False)
    tasks = relationship('Task', back_populates='item')
    board = relationship('Board', back_populates='items')

    def __init__(self, name, board_id, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name
        self.board_id = board_id


    @classmethod
    def get_item_by_name(cls, name, boardName):
        """return an object in the items table with this id"""
        obj = models.storage.get_item_by_name(name, boardName)
        return obj
