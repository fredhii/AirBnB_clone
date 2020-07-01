#!/usr/bin/python3
"""Unittest for class City
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City"""
    def setUp(self):
        """
        Create a new instance of City before each test
        """
        self.c1 = City()

    def tearDown(self):
        """
        Delete City instance before next test
        """
        del self.c1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        c2 = City()
        self.assertNotEqual(self.c1.id, c2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.c1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.c1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.c1.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(City.name), str)

    def test_state_id_type(self):
        """
        Make sure state_id is str data type
        """
        self.assertEqual(type(City.state_id), str)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.c1.updated_at
        self.c1.save()
        self.assertNotEqual(old_updated_at, self.c1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.c1), "[City] ({}) {}".
                         format(self.c1.id, self.c1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.c1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to City instantation
        """
        json_dict = self.c1.to_dict()
        c2 = City(**json_dict)
        self.assertEqual(self.c1.id, c2.id)
        self.assertEqual(self.c1.created_at, c2.created_at)
        self.assertEqual(self.c1.updated_at, c2.updated_at)
        self.assertNotEqual(self.c1, c2)
