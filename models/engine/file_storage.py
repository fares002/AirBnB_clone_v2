#!/usr/bin/python3
"""This module defines a class to manage file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """filestorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all
        """
        dictionary = {}
        if cls:
            dic = self.__objects
            for key in dic:
                part = key.replace('.', ' ')
                part = shlex.split(part)
                if (part[0] == cls.__name__):
                    dictionary[key] = self.__objects[key]
            return (dictionary)
        else:
            return self.__objects

    def new(self, obj):
        """new"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ save
        """
        dictt = {}
        for key, value in self.__objects.items():
            dictt[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dictt, f)

    def reload(self):
        """reload
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete
        """
        if obj:
            obk = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[obk]

    def close(self):
        """ calls
        """
        self.reload()
