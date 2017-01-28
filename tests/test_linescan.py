# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath("."))

import testhelpers
from src import linescan


class TestLineScan(unittest.TestCase):
    """
    Unit tests confirming all linescan scan behavior is correct.
    """
    @classmethod
    def setUpClass(cls):
        global ls
        ls = linescan.LineScan()

    def test_clear_all(self):
        """
        Test running `clear()` with no parameter
        clears the whole cache.
        """
        ls.scan(testhelpers.TEST_FILES_FILE_ONE, 1)
        ls.clear()
        self.assertEqual(len(ls), 0)

    def test_clear_non_existent_file(self):
        """
        Test passing a non-existent file name to `clear()`
        and the cache does not change sizes.
        """
        ls.clear("404-file-not-found.txt")
        self.assertEqual(len(ls), 0)

    def test_clear_single_file(self):
        """
        Test passing a file name to `clear()`
        clears only that file from the cache.
        """
        ls.scan(testhelpers.TEST_FILES_FILE_ONE, 1)
        ls.scan(testhelpers.TEST_FILES_FILE_TWO, 1)
        ls.clear(testhelpers.TEST_FILES_FILE_ONE)
        self.assertEqual(len(ls), 1)

    def test_duplicate_scan_cache(self):
        """Test line scan cache does not change when scan is duplicated."""
        ls.scan(testhelpers.TEST_FILES_FILE_ONE, 6, encoding="utf-8")
        ls.scan(testhelpers.TEST_FILES_FILE_ONE, 6, encoding="utf-8")
        self.assertEqual(len(ls), 2)

    def test_raise_exception_on_error(self):
        """
        Test raising a FileNotFoundError exception
        when a non-existent file is read.
        """
        ls.show_errors(True)
        with self.assertRaises(FileNotFoundError):
            ls.scan("404-file-not-found.txt", 1)

    def test_return_false_on_error(self):
        """Test returning False when an error occurs."""
        ls.show_errors(False)
        result = ls.scan("404-file-not-found.txt", 1)
        self.assertFalse(result)

    def test_scan_multiple_lines_cp1252(self):
        """Test multiple line scanning using cp1252."""
        lines = ls.scan(testhelpers.TEST_FILES_FILE_ONE,
                        8, 9, encoding="cp1252")
        self.assertEqual(lines, """Taken from http://tvipsum.com/
The weather started getting rough - the tiny ship was tossed. If not for the\n""")

    def test_scan_single_line_utf8(self):
        """Test single line scanning using UTF-8."""
        line = ls.scan(testhelpers.TEST_FILES_FILE_ONE, 6, encoding="utf-8")
        self.assertEqual(line, "revolutionary ROI.\n")


if __name__ == "__main__":
    unittest.main()
