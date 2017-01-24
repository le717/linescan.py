# linescan.py [![Build Status](https://travis-ci.org/le717/linescan.py.svg?branch=master)](https://travis-ci.org/le717/linescan.py) #

> Effortlessly read a text file using counting numbers.

Similar to the built-in [`linecache`](http://docs.python.org/3/library/linecache.html) module but designed exclusively for external text files, `linescan.py` is a no-fail module designed to aid beginner programmers who need to read data from text files but have trouble setting up [`open()`](http://docs.python.org/3/library/functions.html#open) or translating real numbers to counting numbers.

### Feature highlight ###
* Uses counting numbers to denote line numbers, removing the need to start counting from zero
* Supports scanning of partial and entire files
* Supports Python 3.3+

## Basic Usage ##
```python
import linescan
LineScan = linescan.LineScan()

# Scan a single line using UTF-8 encoding
LineScan.scan("MyFile.txt", 12, encoding="utf_8")

# Scan multiple lines using default encoding
LineScan.scan("MyFile.txt", 1, 12)
```

More usage can be found in the [`tests`](/tests) directory.

## API Documentation ##
Complete API documentation is available on the [Wiki](https://github.com/le717/linescan.py/wiki/).

## License ##
2013-2017 [Caleb Ely](https://CodeTri.net)

[MIT](LICENSE)
