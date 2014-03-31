# linescan.py [![Build Status](https://travis-ci.org/le717/linescan.py.png?branch=master)](https://travis-ci.org/le717/linescan.py) #

Effortlessly read a text file using counting numbers.

## Features ##

Similar to the built-in [`linecache`](http://docs.python.org/3/library/linecache.html) module but designed exclusively for external text files, `linescan.py` is a no-fail module designed to aid beginner programmers who need to read data from text files but have trouble setting up [`open()`](http://docs.python.org/3/library/functions.html#open) or translating real numbers to counting numbers.

### Feature highlight ###

* Uses counting numbers to denote line numbers, removing the need to start counting from zero
* Supports scanning of partial and entire files
* Stores up to ten previous scans for later retrieval, although the number of stored scans can be change 
* Supports Python 2.7 and 3.3

## Basic Usage ##

```python
import linescan

# Scan a single line using UTF-8 encoding
linescan.scan("MyFile.txt", 12, encoding="UTF-8")

# Scan multiple lines using default encoding
linescan.scan("MyFile.txt", 1, 12)
```

More example usage can be found in the [`examples`](/examples) directory.

## API Documentation ##

Complete API documentation is available on the [Wiki](https://github.com/le717/linescan.py/wiki/).

## License ##

**linescan.py**, created 2013-2014 [Triangle717](http://Triangle717.WordPress.com)
and released under the [The MIT License](http://opensource.org/licenses/MIT).
