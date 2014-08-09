# -*- coding: utf-8 -*-

import sys

parentdir = ".."
# Not happy with editing sys.path... >:-(
sys.path.insert(0, parentdir)
import linescan

__all__ = ["linescan", "testFile"]
testFile = "testfile.txt"
rescanFile = "rescan.txt"
