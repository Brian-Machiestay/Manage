#!/bin/env python3
""" the basemodel where all other models inherit from"""
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid

Base = declarative_base()

class baseMod():
    """the base class for all classes"""
    def __init__(self,*args, **kwargs):
        """initializes a basemodel class"""
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            print("no attributes provided")
        return()

    def to_dict(self):
        """return a dictionary representation of this object"""
        newObj = self.__dict__.copy()
        del(newObj['_sa_instance_state'])
        return newObj

    def save(self):
        """saves obj to the database"""
        models.storage.new(self)
        models.storage.save()

    def close(self):
        """drops the current session"""
        models.storage.close()
