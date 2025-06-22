#!/usr/bin/python3

import json
import os


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_dict = obj.to_dict()
        obj_class = obj_dict["__class__"]
        obj_id = obj_dict["id"]
        FileStorage.__objects[f"{obj_id}.{obj_class}"] = obj_dict

    def save(self):
        if FileStorage.__file_path.strip() != "":
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(FileStorage.__objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
