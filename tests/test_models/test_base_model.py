#!/usr/bin/python3
"""Unittest for class BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel"""
    def setUp(self):
        """
        Create a new instance of BaseModel before each test
        """
        self.b1 = BaseModel()

    def tearDown(self):
        """
        Delete BaseModel instance before next test
        """
        del self.b1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        b2 = BaseModel()
        self.assertNotEqual(self.b1.id, b2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.b1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.b1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.b1.updated_at), datetime)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old_updated_at, self.b1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.b1), "[BaseModel] ({}) {}".
                         format(self.b1.id, self.b1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.b1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to BaseModel instantation
        """
        json_dict = self.b1.to_dict()
        b2 = BaseModel(**json_dict)
        self.assertEqual(self.b1.id, b2.id)
        self.assertEqual(self.b1.created_at, b2.created_at)
        self.assertEqual(self.b1.updated_at, b2.updated_at)
        self.assertNotEqual(self.b1, b2)
