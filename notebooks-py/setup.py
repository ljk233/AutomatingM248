
"""
About
=====
Support script for notebook-py/
Imports src/py/load.py, and changes the wkd to data/
"""

import os

os.getcwd()

os.chdir("..\src\py")

import load

os.chdir("../../data")
