import unittest
from models.base_model import BaseModel, format_datetime_encoding


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def test__str__(self):
        self.assertEqual(
            self.base.__str__(),
            f"[BaseModel] ({self.base.id}) {self.base.__dict__}")

    def test_created_at(self):
        self.assertEqual(self.base.created_at, self.base.created_at)

    def test_to_save(self):
        updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, updated_at)

    def test_to_dict(self):
        created_at = self.base.created_at
        self.base.to_dict()
        self.assertEqual(
            self.base.__dict__["created_at"], created_at.strftime(
                format_datetime_encoding
            )
                        )
        self.assertEqual(self.base.__dict__["__class__"], "BaseModel")
