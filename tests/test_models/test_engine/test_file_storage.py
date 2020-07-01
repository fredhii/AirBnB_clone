#!/usr/bin/python3
"""Unittest for class FileStorage
"""
import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""
    def setUp(self):
        """Store __objects in variable for ease of typing and readability"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path

    def test_objects(self):
        """Test type of __objects"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """Test type of __file_path"""
        self.assertTrue(isinstance(self.file_path, str))

    def test_new(self):
        """Test new works"""
        model = BaseModel()
        length = len(self.objects)
        models.storage.new(model)
        self.assertTrue(length == len(self.objects))

    def test_reload(self):
        """Test reload reloads the object"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """Test reload reloads the object"""
        self.assertTrue(isinstance(self.objects, dict))

class TestBaseModelFileStorage(unittest.TestCase):
    """Test BaseModel file storage"""
    def setUp(self):
        """
        Instantiate new BaseModel object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.b1 = BaseModel()
        self.b1.save()

    def test_basemodel_object_update(self):
        """Test whether new BaseModel objects get added to __objects"""
        self.assertIn('BaseModel.{}'.format(self.b1.id), self.objects.keys())

    def test_basemodel_dict(self):
        """Test if new BaseModel objects' dicts get added to __objects"""
        b1_dict = self.b1.to_dict()
        self.assertIn(b1_dict, self.objects.values())


class TestUserFileStorage(unittest.TestCase):
    """Test User file storage"""
    def setUp(self):
        """
        Instantiate new User object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.u1 = User()
        self.u1.save()

    def test_user_object_update(self):
        """Test whether new User objects get added to __objects"""
        self.assertIn('User.{}'.format(self.u1.id), self.objects.keys())

    def test_user_dict(self):
        """Test whether new User objects' dicts get added to __objects"""
        u1_dict = self.u1.to_dict()
        self.assertIn(u1_dict, self.objects.values())


class TestStateFileStorage(unittest.TestCase):
    """Test State file storage"""
    def setUp(self):
        """
        Instantiate new State object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.s1 = State()
        self.s1.save()

    def test_state_object_update(self):
        """Test whether new State objects get added to __objects"""
        self.assertIn('State.{}'.format(self.s1.id), self.objects.keys())

    def test_state_dict(self):
        """Test whether new State objects' dicts get added to __objects"""
        s1_dict = self.s1.to_dict()
        self.assertIn(s1_dict, self.objects.values())


class TestCityFileStorage(unittest.TestCase):
    """Test City file storage"""
    def setUp(self):
        """
        Instantiate new City object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.c1 = City()
        self.c1.save()

    def test_city_object_update(self):
        """Test whether new City objects get added to __objects"""
        self.assertIn('City.{}'.format(self.c1.id), self.objects.keys())

    def test_city_dict(self):
        """Test whether new City objects' dicts get added to __objects"""
        c1_dict = self.c1.to_dict()
        self.assertIn(c1_dict, self.objects.values())


class TestAmenityFileStorage(unittest.TestCase):
    """Test Amenity file storage"""
    def setUp(self):
        """
        Instantiate new Amenity object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.a1 = Amenity()
        self.a1.save()

    def test_amenity_object_update(self):
        """Test whether new Amenity objects get added to __objects"""
        self.assertIn('Amenity.{}'.format(self.a1.id), self.objects.keys())

    def test_amenity_dict(self):
        """Test whjether new Amenity objects' dicts get added to __objects"""
        a1_dict = self.a1.to_dict()
        self.assertIn(a1_dict, self.objects.values())


class TestPlaceFileStorage(unittest.TestCase):
    """Test Place file storage"""
    def setUp(self):
        """
        Instantiate new Place object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.p1 = Place()
        self.p1.save()

    def test_place_object_update(self):
        """Test whether new Place objects get added to __objects"""
        self.assertIn('Place.{}'.format(self.p1.id), self.objects.keys())

    def test_place_dict(self):
        """Test whether new Place objects' dicts get added to __objects"""
        p1_dict = self.p1.to_dict()
        self.assertIn(p1_dict, self.objects.values())


class TestReviewFileStorage(unittest.TestCase):
    """Test Review file storage"""
    def setUp(self):
        """
        Instantiate new Review object and store private
        attributes into more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.r1 = Review()
        self.r1.save()

    def test_review_object_update(self):
        """Test whether new Review objects get added to __objects"""
        self.assertIn('Review.{}'.format(self.r1.id), self.objects.keys())

    def test_review_dict(self):
        """Test whether new Review objects' dicts get added to __objects"""
        r1_dict = self.r1.to_dict()
        self.assertIn(r1_dict, self.objects.values())
