#!/usr/bin/python3
"""
Here is the class BaseModel
"""


from datetime import datetime
import uuid
import models


formatedTime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initialize the class object"""
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    formatedTime)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    formatedTime)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the baseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                    self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = str(self.__class__.__name__)
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()
        return instanceDict
