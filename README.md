linescan.py
===========

[![Build Status](https://travis-ci.org/le717/linescan.py.png?branch=master)](https://travis-ci.org/le717/linescan.py)

`linescan.py` is a no-fail [Python](http://python.org) module designed to aid in the process the reading single and multiple lines from a text file.

Features
--------

* Uses real line numbers (No need to start counting at 0), making it useful for novice programmers
* Allows specification of file encoding, with fall back to `locale.getpreferredencoding(False)`
* Does not fail, rather, it returns `False` upon encountering any errors
* Supports Python 2.6 - 3.3 plus PyPy


Usage
-----

```python
import linescan
# A single line using UTF-8 encoding
linescan.scanline("MyFile.txt", 3, "utf-8")
# Multiple lines, using the system encoding
linescan.scanlines("MyFile.txt", 3, 6)
# Coming Soon.
```


***linescan.py, created 2013 Triangle717, and released under the [GNU General Public License Version 3](http://www.gnu.org/licenses/gpl.html).**