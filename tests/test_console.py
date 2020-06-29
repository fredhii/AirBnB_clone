#!/usr/bin/python3
""" Console Unit Test """
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestDocumentation(unittest.TestCase):
    """ Validate Console documentation """
    def test_console_pep8(self):
        """ Check console pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0)

    def test_console_docstring(self):
        """ test docstring """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)


class TestConsole(unittest.TestCase):
    """ Console unittest """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance before each test """
        cls.test_console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ Deletes instance after test """
        del cls.test_console

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_emptyline(self):
        """ Test empty line function """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """ Test quit command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """ Test create command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("create test")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("all User")
            self.assertEqual(
                "[\"[User]", f.getvalue()[:8])

    def test_show(self):
        """ Test show command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("show test")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("show BaseModel love")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """ Test destroy command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("destroy test")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("destroy BaseModel love")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """ Test all command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("all test")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("all State")
            self.assertEqual("", f.getvalue())

    def test_update(self):
        """ Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update test")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update User test")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_console.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
