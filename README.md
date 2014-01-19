# linescan.py [![Build Status](https://travis-ci.org/le717/linescan.py.png?branch=master)](https://travis-ci.org/le717/linescan.py) #

Effortlessly read a text file using counting numbers. 

## Features ##

Similar to the built-in [`linecache`](http://docs.python.org/3/library/linecache.html) module but designed exclusively for external text files, `linescan.py` is a no-fail module designed to aid beginner programmers who need to read data from text files but have trouble setting up [`open()`](http://docs.python.org/3/library/functions.html#open) or translating real numbers to counting numbers.

* Uses counting numbers to denote line numbers, removing the need to start counting from `0` (zero)
* Supports both single and multiple lines
* Allows specification of file encoding through `encode` parameter, defaults to `locale.getpreferredencoding(False)`
* Returns `False` upon encountering any errors
* Stores up to `10` (ten) previous scans for later retrieval, stored scans can be deliberately cleared using `linescan.clearscans()`
* Supports Python 2.7 and 3.3 in addition to PyPy

## Usage ##

```python
import linescan

# Deliberately clear all previous stored readings
linescan.clearscans()

# To be written.
```
## License ##

**linescan.py**, created 2013-2014 [Triangle717](http://Triangle717.WordPress.com) and released under the [The MIT License](http://opensource.org/licenses/MIT).
