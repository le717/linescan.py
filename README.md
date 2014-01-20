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

# Deliberately clear all previous stored readings
linescan.clearscans()

# Raise an Exception upon any errors
linescan.showerrors(True)

# To be written.
```

## API Documentation ##

#### linescan.clearscans() ####

* Default: Run automaticlly after `10` (ten) stored scans

> Clear all previously stored readings.

#### linescan.showerrors(_errorValue_) ####

* Default: False

> Option to raise an `Exception` upon any error. Setting _errorValue_ to `True` will raise exceptions,
while setting _errorValue_ to `False` or leaving empty will restore default behavior (`return False`)

#### linescan.scan(_filename_, _lineno_, _endLine=None_, _encoding=None_) ####

> Scan line _alineno_ from a file named _filename_. Specifing  _endLine_ (both implicitly or explicitly)
will scan from _lineno_ to _endLine_.


_To be written._

## License ##

**linescan.py**, created 2013-2014 [Triangle717](http://Triangle717.WordPress.com)
and released under the [The MIT License](http://opensource.org/licenses/MIT).
