#!/bin/env python3
"""create subtasks class"""
from .base import Base, baseMod
from sqlalchemy import String, Numeric, Column

Class Subtask(baseMod, Base):
    """defineds a subtask table"""
    __tablename__ = 'subtasks'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    title = Column(String(64), nullable=False)
    task_id = Column(String(64), ForeignKey('tasks.id'), nullable=False)

    def __init__(self, title, task_id, *args, **kwargs):
        """initializes a subtask instance"""
        self.title = title
        self.task_id = task_id