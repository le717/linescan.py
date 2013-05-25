# /usr/bin/python3
# -*- coding: utf-8 -*-

"""
linescan.py Test Script for Travis CI
"""
import linescan

if __name__ == "__main__":
    line = linescan.scanline("NyanMe20.PiP", 14, None)
    print(line)
    lines = linescan.scanlines("NyanMe20.PiP", 9, 14)
    print(lines)
