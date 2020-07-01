#!/usr/bin/python3
""" FileStorage Unit Test """
import unittest
import models
import pep8
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageDocumentation(unittest.TestCase):
    """ Test FileStorage Documentation """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.user = User()
        cls.user.first_name = "Test"
        cls.user.last_name = "unit"
        cls.user.email = "123@test.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.user

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """ Tests pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """ tests all FileStorage function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ Test new FileStorage function """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 1234567
        user.name = "Test"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """ Test reload FileStorage function """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage """
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path

    def test_objects(self):
        """ Test __objects type """
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """ Test __file_path type """
        self.assertTrue(isinstance(self.file_path, str))

    def test_new(self):
        """ Test new function """
        model = BaseModel()
        length = len(self.objects)
        models.storage.new(model)
        self.assertTrue(length == len(self.objects))

    def test_reload(self):
        """ Test reload function """
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """Test all function"""
        self.assertTrue(isinstance(self.objects, dict))


class TestBaseModelFileStorage(unittest.TestCase):
    """ Test BaseModel """
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.b1 = BaseModel()
        self.b1.save()

    def test_basemodel_object_update(self):
        """ Test update BaseModel __objects """
        self.assertIn('BaseModel.{}'.format(self.b1.id), self.objects.keys())

    def test_basemodel_dict(self):
        """ Test dict BaseModel __objects """
        b1_dict = self.b1.to_dict()
        self.assertIn(b1_dict, self.objects.values())


class TestUserFileStorage(unittest.TestCase):
    """Test User file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.u1 = User()
        self.u1.save()

    def test_user_object_update(self):
        """ Test update User __objects """
        self.assertIn('User.{}'.format(self.u1.id), self.objects.keys())

    def test_user_dict(self):
        """ Test dict User __objects """
        u1_dict = self.u1.to_dict()
        self.assertIn(u1_dict, self.objects.values())


class TestStateFileStorage(unittest.TestCase):
    """Test State file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.s1 = State()
        self.s1.save()

    def test_state_object_update(self):
        """ Test update State __objects """
        self.assertIn('State.{}'.format(self.s1.id), self.objects.keys())

    def test_state_dict(self):
        """ Test dict State __objects """
        s1_dict = self.s1.to_dict()
        self.assertIn(s1_dict, self.objects.values())


class TestCityFileStorage(unittest.TestCase):
    """Test City file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.c1 = City()
        self.c1.save()

    def test_city_object_update(self):
        """ Test update City __objects """
        self.assertIn('City.{}'.format(self.c1.id), self.objects.keys())

    def test_city_dict(self):
        """ Test dict City __objects """
        c1_dict = self.c1.to_dict()
        self.assertIn(c1_dict, self.objects.values())


class TestAmenityFileStorage(unittest.TestCase):
    """Test Amenity file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.a1 = Amenity()
        self.a1.save()

    def test_amenity_object_update(self):
        """ Test update Amenity __objects """
        self.assertIn('Amenity.{}'.format(self.a1.id), self.objects.keys())

    def test_amenity_dict(self):
        """ Test dict Amenity __objects """
        a1_dict = self.a1.to_dict()
        self.assertIn(a1_dict, self.objects.values())


class TestPlaceFileStorage(unittest.TestCase):
    """Test Place file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.p1 = Place()
        self.p1.save()

    def test_place_object_update(self):
        """ Test update Place __objects """
        self.assertIn('Place.{}'.format(self.p1.id), self.objects.keys())

    def test_place_dict(self):
        """ Test dict Place __objects """
        p1_dict = self.p1.to_dict()
        self.assertIn(p1_dict, self.objects.values())


class TestReviewFileStorage(unittest.TestCase):
    """Test Review file storage"""
    def setUp(self):
        """ Creates an instance before each test """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.r1 = Review()
        self.r1.save()

    def test_review_object_update(self):
        """ Test update Review __objects """
        self.assertIn('Review.{}'.format(self.r1.id), self.objects.keys())

    def test_review_dict(self):
        """ Test dict Review __objects """
        r1_dict = self.r1.to_dict()
        self.assertIn(r1_dict, self.objects.values())
