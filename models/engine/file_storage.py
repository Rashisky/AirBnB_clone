#!/usr/bin/env python3
"""Serialization and Deserialization of Instances"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes 
        JSON file to instances
        
        Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=1212, the
        key wil be BaseModel.1212)
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        obj_to_model = {k:BaseModel(**v) for (k,v) in FileStorage.__objects.items()}
        # converts the items in FileStorege_objects to an instance of BaseModel without replacement 
        return obj_to_model
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class>.id"""
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        FileStorage.__objects[f"{self.__class__.__name__}.{self.id}"] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        print("=====================================================")
        print(FileStorage.__objects)
        print("=====================================================")
        
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)
            # {json.dump(key:value) for (key,value) in FileStorage.__objects}
            # for k in FileStorage.__objects:
            #     json.dump(k, file)
    
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise do nothing. if the file doesn't
        exist, no exception should be raised)"""
        if (os.path.exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                obj_py = json.load(file) # converts JSON file to python file
                print(obj_py)
            # Since we may have more than one object/instance of any class, we have to loop
            for keys in obj_py:
                # Also, there is possibility that the instance in question could be instance
                # of any class (e.g BaseModel, etc), thus the need to use there class
                # cls_name = obj_py[keys]["__class__"]
                FileStorage.__objects[keys] = BaseModel(**obj_py[keys]).to_dict() # where ** means it's a dictionary
