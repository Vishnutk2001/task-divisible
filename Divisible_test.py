import Divisible

import pytest

@pytest.fixture
def input():
    x = 20
    return x

def test_divisible_5(input):
    res = Divisible.divisible_5(input)
    assert res == True

def test_divisible_7(input):
    res1 = Divisible.divisible_7(input)
    assert res1 == True

def test_divisible_9(input):
    res2 = Divisible.divisible_9(input)
    assert res2 == True

def test_divisible_10(input):
    res3 = Divisible.divisible_10(input)
    assert res3 == True