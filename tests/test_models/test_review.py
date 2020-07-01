#!/usr/bin/python3
"""Unittest for class Review
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing Review"""
    def setUp(self):
        """
        Create a new instance of Review before each test
        """
        self.r1 = Review()

    def tearDown(self):
        """
        Delete Review instance before next test
        """
        del self.r1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        r2 = Review()
        self.assertNotEqual(self.r1.id, r2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.r1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.r1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.r1.updated_at), datetime)

    def test_place_id(self):
        """
        Make sure place_id is str data type
        """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        """
        Make sure user_id is str data type
        """
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        """
        Make sure text is str data type
        """
        self.assertEqual(type(Review.text), str)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.r1.updated_at
        self.r1.save()
        self.assertNotEqual(old_updated_at, self.r1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.r1), "[Review] ({}) {}".
                         format(self.r1.id, self.r1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.r1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to Review instantation
        """
        json_dict = self.r1.to_dict()
        r2 = Review(**json_dict)
        self.assertEqual(self.r1.id, r2.id)
        self.assertEqual(self.r1.created_at, r2.created_at)
        self.assertEqual(self.r1.updated_at, r2.updated_at)
        self.assertNotEqual(self.r1, r2)
