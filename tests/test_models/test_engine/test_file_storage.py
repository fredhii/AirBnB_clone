#!/usr/bin/python3
""" File Storage Unit Test """
import unittest
import pep8
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestDocumentation(unittest.TestCase):
    """ Check pep8 """
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        f1 = 'models/engine/file_storage.py'
        f2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = pep8style.check_files([f1, f2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestFileStorageMethod(unittest.TestCase):
    """ Test file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def tearDown(self):
        """ Deletes instance after test """
        del self.file_path
        del self.objects

    def test_objects_type(self):
        """ Test private variable type """
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path_type(self):
        """ Check private instance type """
        self.assertTrue(isinstance(self.file_path, str))

    def test_new(self):
        """ Test new function """
        check = BaseModel()
        length = len(self.objects)
        models.storage.new(check)
        self.assertTrue(length == len(self.objects))

    def test_reload_type(self):
        """ Check reload type """
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """ Check objects type """
        self.assertTrue(isinstance(self.objects, dict))


class TestBaseModelFileStorage(unittest.TestCase):
    """ Test BaseModel file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = BaseModel()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after test """
        del self.file_path
        del self.objects
        del self.test

    def test_basemodel_update(self):
        """ Check base model storage """
        self.assertIn('BaseModel.{}'.format(self.test.id), self.objects.keys())

    def test_basemodel_dictionary(self):
        """ Check basemodel to dictionary """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestUserFileStorage(unittest.TestCase):
    """ Test User file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = User()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after a finished test """
        del self.file_path
        del self.objects
        del self.test

    def test_user_update(self):
        """ Check user model storage """
        self.assertIn('User.{}'.format(self.test.id), self.objects.keys())

    def test_user_dict(self):
        """ Check user dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestStateFileStorage(unittest.TestCase):
    """ Test State file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = State()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after test """
        del self.file_path
        del self.objects
        del self.test

    def test_state_update(self):
        """ Check state update """
        self.assertIn('State.{}'.format(self.test.id), self.objects.keys())

    def test_state_dict(self):
        """ Check state dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestCityFileStorage(unittest.TestCase):
    """ Test city file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = City()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after a finished test """
        del self.file_path
        del self.objects
        del self.test

    def test_city_update(self):
        """ Check city model storage """
        self.assertIn('City.{}'.format(self.test.id), self.objects.keys())

    def test_city_dict(self):
        """ Check city dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestAmenityFileStorage(unittest.TestCase):
    """ Test amenity file storage """
    def setUp(self):
        """ Test User file storage """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = Amenity()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after a finished test """
        del self.file_path
        del self.objects
        del self.test

    def test_amenity_update(self):
        """ Check amenity model storage """
        self.assertIn('Amenity.{}'.format(self.test.id), self.objects.keys())

    def test_amenity_dict(self):
        """ Check amenity dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestPlaceFileStorage(unittest.TestCase):
    """ Test Pplace file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = Place()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after a finished test """
        del self.file_path
        del self.objects
        del self.test

    def test_place_update(self):
        """ Check place model storage """
        self.assertIn('Place.{}'.format(self.test.id), self.objects.keys())

    def test_place_dict(self):
        """ Check user dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())


class TestReviewFileStorage(unittest.TestCase):
    """ Test review file storage """
    def setUp(self):
        """ Creates an instance before each test """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.test = Review()
        self.test.save()

    def tearDown(self):
        """ Deletes instance after a finished test """
        del self.file_path
        del self.objects
        del self.test

    def test_review_update(self):
        """ Check review model storage """
        self.assertIn('Review.{}'.format(self.test.id), self.objects.keys())

    def test_review_dict(self):
        """ Check user dicttionary function """
        dictionary = self.test.to_dict()
        self.assertIn(dictionary, self.objects.values())
