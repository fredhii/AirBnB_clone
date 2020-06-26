#!/usr/bin/python3
"""
All the content of the FileStorage class
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """The filestorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialize = {}
        for key in self.__objects:
            serialize[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialize, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists"""
        try:
            with open(self.__file_path, "r") as f:
                file_object = json.load(f)
            for key, value in file_object.items():
                self.__objects[key] = BaseModel(**value)
        except:
            pass
