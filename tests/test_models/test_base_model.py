#!/usr/bin/python3
""" Base Model Unit Test """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseFunctionality(unittest.TestCase):
    """ Test file functionality """
    def setUp(self):
        """ Creates an instance before each test """
        self.test = BaseModel()

    def tearDown(self):
        """ Deletes instance after a test is finished """
        del self.test

    def test_id_type(self):
        """ Check ID type """
        self.assertEqual(type(self.test.id), str)

    def test_unique_id(self):
        """ Check if generates a UUID for every instance """
        test2 = BaseModel()
        self.assertNotEqual(self.test.id, test2.id)

    def test_creationat_type(self):
        """ Check created_at type """
        self.assertEqual(type(self.test.created_at), datetime)

    def test_updatedat_type(self):
        """ Check updated_at type """
        self.assertEqual(type(self.test.updated_at), datetime)

    def test_save_function(self):
        """ Check if update works """
        toUpdate = self.test.updated_at
        self.test.save()
        self.assertNotEqual(toUpdate, self.test.updated_at)

    def test_str(self):
        """ Check __str__ return """
        self.assertEqual(str(self.test),
                         "[BaseModel] ({}) {}".
                         format(self.test.id,
                                self.test.__dict__))

    def test_to_dict(self):
        """ Check dictionary function """
        dictionary = self.test.to_dict()
        self.assertEqual(type(dictionary), dict)
        self.assertTrue(hasattr(dictionary, '__class__'))
        self.assertEqual(type(dictionary['created_at']), str)
        self.assertEqual(type(dictionary['updated_at']), str)

    def test_kwargs(self):
        """ Send kwargs to instance """
        dictionary = self.test.to_dict()
        test2 = BaseModel(**dictionary)
        self.assertEqual(self.test.id,
                         test2.id)
        self.assertEqual(self.test.created_at,
                         test2.created_at)
        self.assertEqual(self.test.updated_at,
                         test2.updated_at)
        self.assertNotEqual(self.test, test2)


if __name__ == "__main__":
    unittest.main()
