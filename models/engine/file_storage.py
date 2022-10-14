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
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

     
    def reload(self):
        new_dict = {}
        if path.exists(self.__file_path):
            with open(self.__file_path) as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(f"{value['__class__']}")(**value)
