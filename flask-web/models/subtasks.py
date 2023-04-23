#!/bin/env python3
"""create subtasks class"""
from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column, ForeignKey, Enum
from sqlalchemy.orm import relationship


class Subtask(baseMod, Base):
    """defineds a subtask table"""
    __tablename__ = 'subtasks'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    title = Column(String(64), nullable=False)
    status = Column(String(32), Enum('checked', 'unchecked'), nullable=False, default='unchecked')
    task_id = Column(String(64), ForeignKey('tasks.id'), nullable=False)
    task = relationship('Task', back_populates='subtasks')

    def __init__(self, title, task_id, status=None, *args, **kwargs):
        """initializes a subtask instance"""
        self.title = title
        self.task_id = task_id
        if status is not None:
            self.status = status
        else:
            self.status = 'unchecked'
