#!/usr/bin/python3
"""Unittest for class State
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Testing State"""
    def setUp(self):
        """
        Create a new instance of State before each test
        """
        self.s1 = State()

    def tearDown(self):
        """
        Delete State instance before next test
        """
        del self.s1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        s2 = State()
        self.assertNotEqual(self.s1.id, s2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.s1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.s1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.s1.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(State.name), str)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.s1.updated_at
        self.s1.save()
        self.assertNotEqual(old_updated_at, self.s1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.s1), "[State] ({}) {}".
                         format(self.s1.id, self.s1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.s1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to State instantation
        """
        json_dict = self.s1.to_dict()
        s2 = State(**json_dict)
        self.assertEqual(self.s1.id, s2.id)
        self.assertEqual(self.s1.created_at, s2.created_at)
        self.assertEqual(self.s1.updated_at, s2.updated_at)
        self.assertNotEqual(self.s1, s2)
