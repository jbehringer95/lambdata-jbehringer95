"""Testing for helper_function"""

import pytest

from helper_functions import null_count, randomize, DF


def test_null_count():
    """Testing the null count function for helper_function"""

    assert null_count(DF) == 2


def test_randomize():
    """Test the randomize function for helper_function"""

    new_DF = randomize(DF, 42)
    assert len(new_DF) == len(DF)
    