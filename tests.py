#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    linescan.py
    Effortlessly read a text file using counting numbers.

    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

    Licensed under The MIT License
    <http://opensource.org/licenses/MIT/>
"""

from __future__ import print_function
import os

import linescan

testFile = os.path.join("examples", "testfile.txt")

if __name__ == "__main__":
    # Scan a single line
    line = linescan.scan(testFile, 5, encoding="utf_8")
    print(line)

    # Scan the same line as above, returns the previous reading.
    lineRepeat = linescan.scan(testFile, 5, encoding="utf_8")
    print(lineRepeat)

    # Scan multiple lines.
    lines = linescan.scan(testFile, 8, 12, encoding="cp1252")
    print(lines)

    # Attempt to read a nonexistant file.
    thisIsFalse = linescan.scan("fake.txt", 55)
    print(thisIsFalse)

    # Any error can be caught by checking it's boolean value.
    if not thisIsFalse:
        print('An error occured while scanning "fake.txt"')

    # Raise an exception upon error.
    #linescan.showerrors(True)

    # Attempt to read the nonexistant file again,
    # but this time with exceptions enabled.
    #thisIsAnException = linescan.scan("fake.txt", 55)

    # Exceptions can be caught using try.. except
    #try:
        #thisIsFalseThree = linescan.scan("fake.txt", 55)
    #except FileNotFoundError:
        #print("ERROR")
