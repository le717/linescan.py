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

    def test_scan_single_line_utf8(self):
        line = ls.scan(testhelpers.TEST_FILES_TESTFILE, 6, encoding="utf-8")
        self.assertEqual(line, "revolutionary ROI.\n")

    def test_scan_multiple_lines_cp1252(self):
        lines = ls.scan(testhelpers.TEST_FILES_TESTFILE,
                        8, 12, encoding="cp1252")
        self.assertEqual(lines, """Taken from http://tvipsum.com/
The weather started getting rough - the tiny ship was tossed. If not for the
courage of the fearless crew the Minnow would be lost. the Minnow would
be lost. So get a witch's shawl on a broomstick you can crawl on. Were
gonna pay a call on the Addams Family. The Love Boat soon\n""")

    def test_clear_all(self):
        ls.clear()
        self.assertEqual(len(ls), 0)

    def test_clear_single_file(self):
        ls.scan(testhelpers.TEST_FILES_TESTFILE, 1)
        ls.clear()
        self.assertEqual(len(ls), 0)

    def test_return_false_on_error(self):
        ls.show_errors(False)
        result = ls.scan("does-not-exist.txt", 1)
        self.assertFalse(result)

    def test_raise_exception_on_error(self):
        ls.show_errors(True)
        with self.assertRaises((IOError, FileNotFoundError)):
            ls.scan("does-not-exist.txt", 1)


if __name__ == "__main__":
    unittest.main()
