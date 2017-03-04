# linescan.py [![Build Status](https://travis-ci.org/le717/linescan.py.svg?branch=master)](https://travis-ci.org/le717/linescan.py) #

> Easily read a text file using counting numbers.

`linescan.py` is a simple module designed to aid beginner programmers who need to read data from text files but have trouble setting up [`open()`](http://docs.python.org/3/library/functions.html#open) or translating real numbers to counting numbers.

### Features ###
* Uses counting numbers to denote line numbers instead of zero-based indexing
* Simple API
* Supports `>=` Python 3.3

## Usage ##
```python
import linescan

# Scan a single line using UTF-8 encoding
linescan.scan("MyFile.txt", 12, 12, encoding="utf-8")

# Scan multiple lines using default encoding
linescan.scan("MyFile.txt", 1, 12)

# Passing a value of `True` will raise Exceptions instead of returning `False`
# Pass a value of `False` to restore default behavior
linescan.show_errors(True)
```

## API Documentation ##
Complete API documentation is available on the [wiki](https://github.com/le717/linescan.py/wiki/).

## License ##
2013-2017 [Caleb Ely](https://CodeTri.net)

[MIT](LICENSE)
