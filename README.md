linescan.py
===========

[![Build Status](https://travis-ci.org/le717/linescan.py.png?branch=master)](https://travis-ci.org/le717/linescan.py)

`linescan.py` is a no-fail [Python 3](http://python.org) module designed to aid in the process the reading single lines from a text file.

Features
--------

* Uses real line numbers (No need to start counting at 0)
* Allows specification of file encoding, with fall back to `sys.getdefaultencoding()`
* Does not fail, rather, it quietly supresses any errors


Usage
-----

The best way to explain how it works is by example, or by running `help(linescan)`.

```python
import linescan
linescan.scanline("MyFile.txt", 3, "utf-8")
# Coming Soon.
```
