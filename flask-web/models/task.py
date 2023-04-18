#!/bin/env python3
"""create a db model to handle all tasks"""

from base import Base, baseMod
from sqlalchemy import String, Numeric, Column

class Task(baseMod, Base):
    """define methods on this class's instances"""
    __tablename__ = 'tasks'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    

    def __init__(self, name, board_id, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        
