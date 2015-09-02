## Synopsis

Class that has two functions: verify if a given word is a palindrome, and to spell check in ptbr a word or phrase

## Dependencies

- Python 2.x
- Uses os, re, collections and argparse, that are default on python 2.5
- Uses setutools

## Installation

#First, install setuptools

https://pypi.python.org/pypi/setuptools#installation-instructions

#Second, install from source
As root, run on the cloned folder:
```unix
python setup.py install
```

#Or install from egg package
As root, run on downloaded egg:
```unix
easyinstall words-1.0-py2.7.egg
```

## Runing without an instalator
First, enter in the cloned folder.  Then:
```unix
cd words
```
To use  it type the below command your Linux / Mac terminal, and it will give more instructions
```unix
python words_parses.py --help
```

##Known Issues

Spell check on special characters does not work well with python 2.x, because the "re" lib does not give full support to utf-8

##TODO

Make it work with python 3.x

## License

You are free to use this code under the MIT license: 
http://www.opensource.org/licenses/mit-license.php
