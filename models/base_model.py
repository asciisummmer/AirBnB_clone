#!/usr/bin/python3

""" Base model implementation
"""
import uuid
from datetime import datetime

format_datetime_encoding = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.strftime(
            format_datetime_encoding
            )
        self.__dict__["updated_at"] = self.updated_at.strftime(
            format_datetime_encoding
            )
        return self.__dict__
