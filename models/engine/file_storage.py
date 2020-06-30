#!/usr/bin/python3
"""
All the content of the FileStorage class
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
(__file_path) exists"""
        try:
            with open(self.__file_path, "r") as f:
                file_object = json.load(f)
            for key, value in file_object.items():
                kwav =  eval(value['__class__'])(**value)
                self.__objects[key] = kwav
        except:
            pass
  
