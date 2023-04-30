#!/bin/env python3
"""create a user model for logging users into the database"""
from models.base import Base, baseMod
from flask_login import UserMixin
from sqlalchemy import String, Numeric, Column, Boolean
from sqlalchemy.orm import relationship

class User(UserMixin, baseMod, Base):
    """a model for users in this application"""
    __tablename__ = 'users'
    id = Column(String(132), primary_key=True, nullable=False, unique=True)
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    boards = relationship('Board', back_populates='user')

