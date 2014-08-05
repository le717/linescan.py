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
from __init__ import (linescan, testFile)


def main():
    lineScan = linescan.LineScan()
    # Scan the first nine lines of the file individually.
    print("\n------- Scanning lines 1-11 of testfile.txt ------- \n")
    for i in range(1, 11):
        line = lineScan.scan(testFile, i, encoding="utf_8")

        # Enable number of stored scans debug value.
        numOfScans = lineScan.debug(scannum=True)

        # Display the results of our scans.
        print("Line #{0}:\n{1}".format(numOfScans, line))

    # First example, automatic clearing of stored scans.
    print("\n------- Example #1 -------\n")

    # Read the fifteenth line and watch as the stored scans are cleared.
    lineEleven = lineScan.scan(testFile, 15, encoding="utf_8")
    print("Stored scan #{0}, Line #15:\n{1}".format(
          lineScan.debug(scannum=True), lineEleven))

    # Second example, manual clearing.
    print("\n------- Example #2 -------\n")

    # Read line 13 of testfile.txt
    lineThirteen = lineScan.scan(testFile, 13, encoding="utf_8")
    print("Stored scan #{0}, Line #13:\n{1}".format(
          lineScan.debug(scannum=True), lineThirteen))

    # To clear stored scans manually, simply run
    lineScan.clearscans()

    # And we will see the scans are no more
    print("Number of stored scans: {0}".format(lineScan.debug(scannum=True)))

    # Third example, recalling a stored scan.
    print("\n------- Example #3 -------\n")

    # Read lines 1-3 all at once
    threeLines = lineScan.scan(testFile, 1, 3, encoding="utf_8")
    print("Stored scan #{0}, Lines #1-3:\n{1}".format(
          lineScan.debug(scannum=True), threeLines))

    # Later on, we may need to refer to those lines again.
    # Instead of marking the variable as global,
    # Simply run the same line again.
    print()
    threeLinesRepeat = lineScan.scan(testFile, 1, 3, encoding="utf_8")
    print("Stored scan #{0}, Lines #1-3:\n{1}".format(
          lineScan.debug(scannum=True), threeLinesRepeat))

    # As your can see, the number of stored scans did not change.
    # Rather, the previous scan was retrieved. This helps increase speed by
    # not requiring the file to be re-scanned for the exact same information!

    try:
        raw_input("\nPress Enter to close.")
    except NameError:
        input("\nPress Enter to close.")
    raise SystemExit(0)

if __name__ == "__main__":
    main()
