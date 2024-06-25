import unittest
from get_digits import *

class test_get_digits(unittest.TestCase):

    def test_get_digits(self):
        s = get_digits("<0.12-34 56abc789x")
        self.assertEqual(list("0123456789"),
                         get_digits(s))
        self.assertEqual(list("1230"),
                         get_digits(1230))

unittest.main()
