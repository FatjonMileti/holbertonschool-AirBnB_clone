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
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                for key, value in (json.load(f)).items():
                    FileStorage.__objects[key] = eval(f"{value['__class__']}")(**value)
