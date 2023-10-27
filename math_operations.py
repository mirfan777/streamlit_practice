# streamlit_calculator.py

import streamlit as st


def add(x, y):
    """Return sum of x and y.
    >>> add(1,2)
    3
    >>> add(2,4)
    6
    """
    return x + y


def subtract(x, y):
    """Return subtract of x and y.
    >>> subtract(2,2)
    0
    >>> subtract(4,2)
    2
    """
    return x - y


def multiply(x, y):
    """Return multiply of x and y.
    >>> multiply(1,2)
    2
    >>> multiply(2,4)
    8
    """
    return x * y


def divide(x, y):
    """Return divide of x and y.
    >>> divide(2,1)
    2.0
    >>> divide(15,3)
    5.0
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y


import doctest
doctest.testmod()