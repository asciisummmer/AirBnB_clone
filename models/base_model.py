#!/usr/bin/python3

""" Base model implementation
"""
import uuid
import datetime

class BaseModel:

    def __init__(self, ):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now() 
        self.updated_at = datetime.now()

    def __str__(self):
        return "self.__class__.__name__"

