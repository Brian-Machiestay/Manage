#!/usr/bin/env python3
"""defines the storage class
"""
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models.board import Board
from models.items import Item
from models.task import Task
from models.subtasks import Subtask
import sqlalchemy


classes = {'Board': Board, 'Item': Item, 'Task': Task, 'Subtask': Subtask}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('brian',
                                             'developer',
                                             'localhost',
                                             'manage'))

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def all(self, cls):
        """
        Returns the object based on the class name and its and ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.__session.query(cls).all()
        return all_cls

    def one(self, cls, id):
        """return one object of a class"""
        allobjs = self.__session.query(cls).filter_by(id=id).first()
        return allobjs

    def board_by_name(self, name):
        """return an object based on it's name"""
        obj = self.__session.query(Board).filter_by(name=name).first()
        return obj

    def get_other_boards(self, name):
        """return board objs not equal this board"""
        obj = self.__session.query(Board).filter(Board.name != name).limit(2).all()
        return obj

    def get_item_by_name(self, name, boardName):
        """return the item based on this id"""
        obj = self.__session.query(Item).join(Board, Item.board_id==Board.id)\
                                        .filter(Item.name==name,
                                                Board.name==boardName).first()
        return obj
