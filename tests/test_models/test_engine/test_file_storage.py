#!/usr/bin/python3
""" FileStorage Unit Test """

import unittest
import pep8
import json
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import datetime


class TestFileStorage(unittest.TestCase):
    """ test FileStorage """

    def test_docstrings(self):
        """ Tests for dosctrings """
        self.assertGreater(len(file_storage.__doc__), 1)
        self.assertGreater(len(FileStorage.__doc__), 1)
        self.assertGreater(len(FileStorage.all.__doc__), 1)
        self.assertGreater(len(FileStorage.new.__doc__), 1)
        self.assertGreater(len(FileStorage.save.__doc__), 1)
        self.assertGreater(len(FileStorage.reload.__doc__), 1)

    def test_pep8(self):
        """ Test PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        base_model_path = 'models/engine/file_storage.py'
        result_base_model = pep8_val.check_files([base_model_path])
        self.assertEqual(result_base_model.total_errors, 0)
        t_model_path = 'tests/test_models/test_engine/test_file_storage.py'
        result_test_base_model = pep8_val.check_files([t_model_path])
        self.assertEqual(result_test_base_model.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
