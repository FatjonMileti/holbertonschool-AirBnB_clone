#!/usr/bin/python3
import json
from os import path

class FileStorage:

    __file_path = objects.json
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = self.__class__.__name__ + '.' + obj.id
        self.__objects[key]  = obj

    def save(self):
        pass    
     
    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
            for k, v in json_dict.items():
                self.__objects[k] = eval(v['__class__'])(**v)