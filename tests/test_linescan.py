# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(".."))

import testhelpers
from src import linescan


class TestLineScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global ls
        ls = linescan.LineScan()

    def test_clear_all(self):
        ls.clear()
        self.assertEqual(len(ls), 0)

    def test_clear_single_file(self):
        ls.scan(os.path.join(testhelpers.TEST_FILES_ROOT_PATH, "testfile.txt"), 1)
        ls.clear()
        self.assertEqual(len(ls), 0)


if __name__ == "__main__":
    unittest.main()
