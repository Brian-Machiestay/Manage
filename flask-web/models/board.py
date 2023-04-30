#!/bin/env python3
"""model to create a board object"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column, ForeignKey
from sqlalchemy.orm import relationship
import models

class Board(baseMod, Base):
    """defines a board table"""
    __tablename__ = 'board'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    name = Column(String(64), nullable=False, unique=True)
    user_id = Column(String(64), ForeignKey('users.id'), nullable=False)
    items = relationship('Item', back_populates='board')
    user = relationship('User', back_populates='boards')

    def __init__(self, name, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.name = name


    @classmethod
    def boards(cls, user_id):
        """return a board based on it's id"""
        this_board = models.storage.all(cls, user_id)
        return this_board

    @classmethod
    def board(cls, user_id, id):
        """return a single board based on the id"""
        bd = models.storage.one(cls, user_id, id)
        return bd

    @classmethod
    def board_by_name(cls, user_id, name):
        """return a board based on its name"""
        bd = models.storage.board_by_name(user_id, name)
        return bd

    @classmethod
    def get_other_boards(cls, user_id, name):
        """return two boards whose name do not equal name"""
        bd = models.storage.get_other_boards(user_id, name)
        return bd

    @classmethod
    def count_boards(cls, user_id):
        """count the number of boards"""
        cnt = models.storage.count(Board, user_id)
        return cnt
