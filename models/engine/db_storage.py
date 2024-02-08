#!/usr/bin/python3
"""New engine DBStorage module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage Class"""
    __engine = None
    __session = None
    __classes = {"State": State, "Amenity": Amenity,
                 "City": City, "Place": Place,
                 "Review": Review, "User": User}

    def __init__(self):
        """init function"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
        ), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadate.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dictionary = {}
        if cls is None:
            for cl in DBStorage.__classes.values():
                objects = self.__session.query(cl).all()
                for obj in objects:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    dictionary[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f'{obj.__class__.__name__}.{obj.id}'
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        # if obj is not None:
        self.__session.delete(obj)

    def reload(self):
        """The reload function"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
