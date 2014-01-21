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
# -*- coding: utf-8 -*-

from __init__ import linescan


def main():

    # Raise an exception upon error.
    linescan.showerrors(True)

    # Exceptions can be caught using try... except blocks.s
    try:
        # Attempt to read a nonexistant file
        linescan.scan("fake.txt", 55)
    except FileNotFoundError:
        print("Error reading fake.txt")

    # Attempt to read the nonexistant file again,
    # but this time without catching the error
    linescan.scan("fake.txt", 55)

if __name__ == "__main__":
    main()
