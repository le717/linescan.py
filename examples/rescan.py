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
from __init__ import (linescan,
                      autoRun,
                      rescanFile
                     )


def main():

    LineScan = linescan.LineScan()
    # Scan the line
    line = LineScan.scan(rescanFile, 1, encoding="utf_8")
    print("\nFile scan:\n{0}".format(line))

    # Next, rewrite the file contents
    with open(rescanFile, "wt") as f:
        f.write("Hello!\n")

    # Now we rescan the file, ensuring we reassign the `line` variable
    # to get the updated contents
    line = LineScan.rescan(rescanFile)
    print("File rescan:\n{0}".format(line))

    # Finally, rewrite the original file contents for next time
    with open(rescanFile, "wt") as f:
        f.write("Hello, World!\n")

    if not autoRun:
        try:
            raw_input("\nPress Enter to close.")
        except NameError:
            input("\nPress Enter to close.")
        raise SystemExit(0)

if __name__ == "__main__":
    main()
