#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = self.__class__.__name__ + '.' + self.id
        self.__objects[key]  = obj

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__objects))
     
    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path) as f:
                json_dict = json.loads(f.read())
            for key, value in json_dict.items():
                self.__object[key] = BaseModel(**value)
