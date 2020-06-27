#!/usr/bin/python3
""" Place Model Unit Test """
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestDocumentation(unittest.TestCase):
    """ Check pep8 """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        f1 = 'models/place.py'
        f2 = 'tests/test_models/test_place.py'
        result = pep8style.check_files([f1, f2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestPlace(unittest.TestCase):
    """Testing Place"""
    def setUp(self):
        """ Creates an instance before each test """
        self.test = Place()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_uniqueUUID(self):
        """ Check if generates a UUID for every instance """
        test2 = Place()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(Place.name), str)

    def test_city_id(self):
        """ Test city-id type """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """ Test user_id type """
        self.assertEqual(type(Place.user_id), str)

    def test_description(self):
        """ Test description type """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """ Test number_rooms type """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test number_bathrooms type """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """ Test max_guest type """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """ Test price by nigth type """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitutde(self):
        """ Test latitude type """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """ Test longitude type """
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """ Check amenity_ids type """
        self.assertEqual(type(Place.amenity_ids), list)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test), "[Place] ({}) {}".
                         format(self.test.id, self.test.__dict__))

    def test_dictionary(self):
        """ Check to_dict function """
        dictionary = self.test.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertTrue(hasattr(dictionary, '__class__'))
        self.assertEqual(type(dictionary['created_at']), str)
        self.assertEqual(type(dictionary['updated_at']), str)

    def test_kwargs(self):
        """ Validate kawrgs arguments """
        dictionary = self.test.to_dict()
        test2 = Place(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)
