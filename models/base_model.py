#!/usr/bin/python3

"""
"""
import uuid
import datetime

class BaseModel:
    """
    """

    def __init__(self):
        my_id = uuid.uuid4()
        self.id = str(my_id)
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dicto = {'__class__': type(self).__name__ ,
                 'created_at': str(self.created_at).replace(' ', 'T'),
                 'updated_at': str(self.updated_at).replace(' ', 'T')
                }
        self.__dict__.update(dicto)
        return self.__dict__

    def __str__(self):
        print(f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
