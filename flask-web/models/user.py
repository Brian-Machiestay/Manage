#!/bin/env python3
"""create a user model for logging users into the database"""
from models.base import Base, baseMod

class User(baseMod, Base):
    """a model for users in this application"""
    
