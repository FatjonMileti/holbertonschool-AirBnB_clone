#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = self.__class__.__name__ + '.' + self.id
        FileStorage.__objects[key] = obj

    def save(self):
        newdict = {}
        for key, value in FileStorage.__objects.items():
            newdict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(newdict, f)

     
    def reload(self):
        newdict =  {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                newdict = json.load(f)
            for key, value in newdict.items():
                 FileStorage.__objects[key] = BaseModel(**value)
