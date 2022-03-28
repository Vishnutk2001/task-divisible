import Divisible

import pytest

def test_divisible_5():
    x = 20
    res = Divisible.divisible_5(x)
    assert res == True

def test_divisible_7():
    x = 14
    res1 = Divisible.divisible_7(x)
    assert res1 == True

def test_divisible_9():
    x = 18
    res2 = Divisible.divisible_9(x)
    assert res2 == True

def test_divisible_10():
    x = 20
    res3 = Divisible.divisible_10(x)
    assert res3 == True