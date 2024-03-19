#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dicationary = {}
        if cls:
            dic = self.__objects
            for k in dic:
                part = k.replace('.', ' ')
                part = shelx.split(part)
                if (part[0] == cls.__name__):
                    dicationary[k] = self.__objects[k]
            return (dicationary)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """Saves storage dictionary to file"""
        dictt = {}
        for k, v in self.__objects.items():
            dictt[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dictt, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for k, value in
(json.load(f)).items():
                    value = eval(value["__class__"])
(**value)
                    self.__objects[k] = value 
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[k]

    def close(self):
        """ calls"""
        self.reload()
