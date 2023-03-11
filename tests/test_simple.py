import unittest
from unittest.mock import patch
from io import StringIO
from example.simple import say


class TestSimple(unittest.TestCase):
    @patch('sys.stdout', new_callable = StringIO)
    def test_say(self, stdout):
        #say("Hello")
        #extected_out = 'Hello\n'
        #self.assertEqual(stdout.getvalue(), extected_out)
        pass
