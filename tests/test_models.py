"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0],[0, 0],[0, 0]], [0,0]),
        ([[1, 2],[3, 4],[5, 6]], [3,4]),
    ]
)
def test_daily_mean(test, expected):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0],[0, 0],[0, 0]], [0,0]),
        ([[1, 2],[13, 4],[5, 6]], [13,6]),
    ]
)
def test_daily_max(test, expected):
    """Test that max function finds max from array of positive or negative integers"""
    from inflammation.models import daily_max

     #Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0],[0, 0],[0, 0]], [0,0]),
        ([[1, 2],[-3, 4],[5, 6]], [-3,2]),
    ]
)
def test_daily_min(test, expected):
    """Test that min function finds min from array of positive or negative integers"""
    from inflammation.models import daily_min

     #Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test), expected)


@pytest.mark.parametrize(
    "test",
    [
        ([['abc', 'asd'], ['zxy', 'xyz']]),
        ([['ghj', 'jhg'], ['lkj', 'jkl']]),
    ]
)
def test_daily_min_string(test):
    from inflammation.models import daily_min
    with pytest.raises(TypeError):
        error_expected = daily_min(test)

