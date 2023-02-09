#!/usr/bin/env python3
"""Defines all common attributes/methods for other classes
"""
import uuid
import datetime

class BaseModel:
    """The base class that contains all methods and attributes"""
    
    def __init__(self):
        """Instantiate the id, when id is created and updated"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        result = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return result
    
    def save(self):
        """updates the public instance attribute and save"""
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all keys/value of __dict__
        of the instance"""
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
