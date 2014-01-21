# linescan.py [![Build Status](https://travis-ci.org/le717/linescan.py.png?branch=master)](https://travis-ci.org/le717/linescan.py) #

Effortlessly read a text file using counting numbers.

## Features ##

Similar to the built-in [`linecache`](http://docs.python.org/3/library/linecache.html) module but designed exclusively for external text files, `linescan.py` is a no-fail module designed to aid beginner programmers who need to read data from text files but have trouble setting up [`open()`](http://docs.python.org/3/library/functions.html#open) or translating real numbers to counting numbers.

* Uses counting numbers to denote line numbers, removing the need to start counting from `0` (zero)
* Stores up to `10` (ten) previous scans for later retrieval, stored scans can be deliberately cleared using `linescan.clearscans()`
* Allows specification of file encoding using `encoding` parameter, defaults to `locale.getpreferredencoding(False)`
* Returns `False` upon encountering any errors, `Exceptions` can be raised using `linescan.showerrors(True)`
* Supports Python 2.7 and 3.3 in addition to PyPy

## Basic Usage ##

```python
import linescan

linescan.scan("MyFile.txt")

# To be written.
```

## API Documentation ##

API Documentation is available on the [Wiki](https://github.com/le717/linescan.py/wiki/).

## License ##

**linescan.py**, created 2013-2014 [Triangle717](http://Triangle717.WordPress.com)
and released under the [The MIT License](http://opensource.org/licenses/MIT).
