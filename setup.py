from distutils.core import setup

setup(
    name="linescan.py",
    version="1.2.0",
    author="Triangle717",
    author_email="le717.code@yahoo.com",
    url="https://github.com/le717/linescan.py",
    download_url="https://github.com/le717/linescan.py/archive/v1.2.0.tar.gz",

    description="Effortlessly read a text file using counting numbers.",
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers"
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable"
    ],

    py_modules=['linescan'],

    long_description="""Similar to the built-in `linecache` module but designed
exclusively for external text files, linescan.py is a no-fail module designed
to aid beginner programmers who need to read data from text files but have
trouble setting up `open()` or translating real numbers to counting numbers.

linescan.py supports Python 2.7, Python 3.3+, and PyPy.""",
)
