#!/usr/bin/env python3
"""defines the storage class
"""
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models.board import Board
from models.items import Item
from models.task import Task
from models.user import User
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

    def all(self, cls, user_id):
        """
        Returns the object based on the class name and its and ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.__session.query(Board).join(User, User.id==Board.user_id)\
                                             .filter(User.id==user_id).all()
        return all_cls

    def one(self, cls, user_id, id):
        """return one object of a class"""
        obj = self.__session.query(cls).join(User, User.id==Board.user_id)\
                                       .filter(User.id==user_id,
                                               Board.id==id).first()
        return obj

    def board_by_name(self, user_id, name):
        """return an object based on it's name"""
        obj = self.__session.query(Board).join(User, User.id==Board.user_id)\
                                         .filter(User.id==user_id,
                                                 Board.name==name).first()
        return obj

    def get_other_boards(self, user_id, name):
        """return board objs not equal this board"""
        obj = self.__session.query(Board).join(User, User.id==Board.user_id)\
                                         .filter(Board.name != name,
                                                 User.id==user_id)\
                                         .limit(2).all()
        return obj

    def get_item_by_name(self, user_id, name, boardName):
        """return the item based on this id"""
        obj = self.__session.query(Item).join(User, User.id==Board.user_id)\
                                        .join(Board, Item.board_id==Board.id)\
                                        .filter(Item.name==name,
                                                Board.name==boardName,
                                                User.id==user_id).first()
        return obj

    def count(self, cls, user_id):
        """return the number of objects in cls for a particular user"""
        cnt = self.__session.query(Board).join(User, User.id==Board.user_id)\
                                         .filter(User.id==user_id).count()
        return cnt


    # user management methods
    def user_by_email(self, email):
        """return user with this email"""
        return self.__session.query(User).filter_by(email=email).first()


    def user_by_id(self, id):
        """return a user based on it's id"""
        return self.__session.query(User).filter_by(id=id).first()
