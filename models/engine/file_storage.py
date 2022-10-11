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
        