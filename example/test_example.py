"""Basic Unit testing for example.py"""

import math
from random import randint
import pytest
from example import increment, COLORS

def test_increment():
    """testing increment function"""
    test_value = randint(100, 1000)

    assert increment(3) == 4
    # TODO Stretch goal - How can I test negative floats?
    assert increment(-2) == -1
    assert increment(2.8) == 3.8

    def test_increment_floats():
        """Testing postive floats for increment functions"""

        assert increment(2.8) == 3.8
        assert increment(10.8) == 11.8



    

