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
from __init__ import linescan


def main():

    # Attempt to read a nonexistent file,
    # retaining the default error setting.
    if not linescan.scan("fake.txt", 55):
        print("""Example #1: Error reading fake.txt
Returned error value is `False`.
""")

    # Enable option to raise an exception upon any error.
    linescan.showerrors(True)

    # Attempt to read the nonexistent file again,
    # but this time catch the Exception
    # using an try...except block.
    try:
        linescan.scan("fake.txt", 55)
    except (OSError, FileNotFoundError):  # noqa
        print("""Example #2: Error reading fake.txt
Returned error value is as an `OSError` or `FileNotFoundError`.
The exception was caught with a try...except block.
""")

    # Finally, read the nonexistent a third time,
    # but this time without catching the Exception.
    print("""Example #3: Error reading fake.txt
Returned error value is as an `OSError or FileNotFoundError`.
The exception was not caught with a try...except block.
""")
    linescan.scan("fake.txt", 55)

    try:
        raw_input("\nPress Enter to Exit.")
    except NameError:
        input("\nPress Enter to Exit.")
    finally:
        raise SystemExit(0)

if __name__ == "__main__":
    main()
