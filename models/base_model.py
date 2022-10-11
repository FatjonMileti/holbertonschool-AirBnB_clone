#!/usr/bin/python3
"""Task3 """
from time import strptime
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """Super class, define by id, created_at, updated_at"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key,value in kwargs.items():
                
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, "%A %d %B %Y at %H:%M:%S"))
                elif key == '__class__':
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """returns dict"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """public method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """public method"""
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.strftime("%A %d %B %Y at %H:%M:%S")
        d['updated_at'] = self.created_at.strftime("%A %d %B %Y at %H:%M:%S")
        return d
