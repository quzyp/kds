import pathlib
import sys
import unittest

project_root = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(project_root)

from kds import create_app

class TestConfig(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(0, 0)