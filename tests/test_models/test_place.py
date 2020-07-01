#!/usr/bin/python3
"""Unittest for class Place
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place"""
    def setUp(self):
        """
        Create a new instance of Place before each test
        """
        self.p1 = Place()

    def tearDown(self):
        """
        Delete Place instance before next test
        """
        del self.p1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        p2 = Place()
        self.assertNotEqual(self.p1.id, p2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.p1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.p1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.p1.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(Place.name), str)

    def test_city_id(self):
        """
        Make sure city_id is str data type
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """
        Make sure user_id is str data type
        """
        self.assertEqual(type(Place.user_id), str)

    def test_description(self):
        """
        Make sure description is str data type
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """
        Make sure number_rooms is int data type
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Make sure number_bathrooms is int data type
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """
        Make sure max_guest is int data type
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """
        Make sure price_by_night is int data type
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitutde(self):
        """
        Make sure latitude is float
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """
        Make sure longitude is float
        """
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """
        Make sure amenity_ids is a list
        """
        self.assertEqual(type(Place.amenity_ids), list)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.p1.updated_at
        self.p1.save()
        self.assertNotEqual(old_updated_at, self.p1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.p1), "[Place] ({}) {}".
                         format(self.p1.id, self.p1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.p1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to Place instantation
        """
        json_dict = self.p1.to_dict()
        p2 = Place(**json_dict)
        self.assertEqual(self.p1.id, p2.id)
        self.assertEqual(self.p1.created_at, p2.created_at)
        self.assertEqual(self.p1.updated_at, p2.updated_at)
        self.assertNotEqual(self.p1, p2)
