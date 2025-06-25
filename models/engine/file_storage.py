#!/usr/bin/python3

import json
import os
from ..base_model import BaseModel


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_dict = obj.to_dict()
        obj_class = obj_dict["__class__"]
        obj_id = obj_dict["id"]
        FileStorage.__objects[f"{obj_class}.{obj_id}"] = obj

    def save(self):
        if FileStorage.__file_path.strip() != "":
            objects_dict = {}
            for key in FileStorage.__objects:
                objects_dict[key] = FileStorage.__objects[key].to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(objects_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                objects_dict = json.load(file)

            for key, value in objects_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
