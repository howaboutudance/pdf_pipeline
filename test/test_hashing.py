import fcshash
from unittest import TestCase
import tempfile

class TestHash(TestCase):
    def setUp(self):
        self.test_basic_file = tempfile.TemporaryFile("r")

    def test_hash_basic_file(self):
        self.assertTrue(self.test_basic_file)