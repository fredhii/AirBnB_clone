#!/usr/bin/python3
""" City Model Unit Test """
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestDocumentation(unittest.TestCase):
    """ Check pep8 """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        f1 = 'models/city.py'
        f2 = 'tests/test_models/test_city.py'
        result = pep8style.check_files([f1, f2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCityModel(unittest.TestCase):
    """ Test City """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = City()

    def tearDown(self):
        """ Deletes instance after a test """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = City()
        self.assertNotEqual(self.test.id, test2.id)

    def test_created_at_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updated_at_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_city_type(self):
        """ Check city type """
        self.assertEqual(type(City.name), str)

    def test_state_id_type(self):
        """ Check state_id type """
        self.assertEqual(type(City.state_id), str)

    def test_save(self):
        """ Test save function """
        check = self.test.updated_at
        self.test.save()
        self.assertNotEqual(check, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[City] ({}) {}".
                         format(self.test.id,
                                self.test.__dict__))

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
        test2 = City(**dictionary)
        self.assertEqual(self.test.id, test2.id)
        self.assertEqual(self.test.created_at, test2.created_at)
        self.assertEqual(self.test.updated_at, test2.updated_at)
        self.assertNotEqual(self.test, test2)
