# -*- coding: utf-8 -*-

import sys

parentdir = ".."
# Not happy with editing sys.path... >:-(
sys.path.insert(0, parentdir)
import linescan

__all__ = ("linescan", "autoRun", "rescanFile", "testFile")
try:
    if sys.argv[1] == "travis":
        autoRun = True
except IndexError:
    autoRun = False

# Define files to use for examples
testFile = "testfile.txt"
rescanFile = "rescan.txt"
