#!/bin/env python3
"""create a db model to handle all tasks"""

from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column, ForeignKey
from sqlalchemy.orm import relationship

class Task(baseMod, Base):
    """define methods on this class's instances"""
    __tablename__ = 'tasks'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    item_id = Column(String(132), ForeignKey('items.id'), nullable=False)
    title = Column(String(132), nullable=False, unique=True)
    description = Column(String(1024), nallable=False)
    item = relationship('Item', back_populates='tasks')
    subtasks = relationship('Subtask', back_populates='task')
    

    def __init__(self, tit, des, item_id, *args, **kwargs):
        """initialize an instance of this class"""
        super().__init__(self, *args, **kwargs)
        self.title = tit
        self.description = des
        self.item_id = item_id
