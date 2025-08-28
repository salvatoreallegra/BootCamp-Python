# -------------------------------------------------------
# test_functions.py
# Unit tests for greet() and add()
# -------------------------------------------------------
from bootcamp_python.day03.day03_functions import greet, add

def test_greet_returns_string():
    assert greet("Sal") == "Hello, Sal!"

def test_add_two_ints():
    assert add(2, 3) == 5

def test_add_floats():
    assert add(2.5, 0.5) == 3.0
