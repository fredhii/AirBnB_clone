#!/usr/bin/python3
"""Unittest for class User
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User"""
    def setUp(self):
        """
        Create a new instance of User before each test
        """
        self.u1 = User()

    def tearDown(self):
        """
        Delete User instance before next test
        """
        del self.u1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        u2 = User()
        self.assertNotEqual(self.u1.id, u2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.u1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.u1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.u1.updated_at), datetime)

    def test_email_type(self):
        """
        Make sure email is str data type
        """
        self.assertEqual(type(User.email), str)

    def test_password_type(self):
        """
        Make sure password is str data type
        """
        self.assertEqual(type(User.password), str)

    def test_first_name_type(self):
        """
        Make sure first_name is str data type
        """
        self.assertEqual(type(User.first_name), str)

    def test_last_name_type(self):
        """
        Make sure last_name is str data type
        """
        self.assertEqual(type(User.last_name), str)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.u1.updated_at
        self.u1.save()
        self.assertNotEqual(old_updated_at, self.u1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.u1), "[User] ({}) {}".
                         format(self.u1.id, self.u1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.u1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to User instantation
        """
        json_dict = self.u1.to_dict()
        u2 = User(**json_dict)
        self.assertEqual(self.u1.id, u2.id)
        self.assertEqual(self.u1.created_at, u2.created_at)
        self.assertEqual(self.u1.updated_at, u2.updated_at)
        self.assertNotEqual(self.u1, u2)
