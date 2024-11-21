
from log import log
import random
import math


def test_works_for_exact_power():
    assert log(3, 81) == 4


def test_works_for_inexact_power():
    assert log(2, 7) == 2


def test_works_if_a_is_greater_than_b():
    assert log(2, 1) == 0


def test_works_if_division_would_skip_over_1():
    assert log(3, 8) == 1


def test_matches_math_library():
    for i in range(100):
        a = random.randint(2, 10)
        b = random.randint(1, 1000000000)
        assert log(a, b) == math.floor(math.log(b, a))
#def test_finds_logs_when_a_less():
 #   assert logs(2,20) == 4

#def test_finds_logs_when_a_greater():
 #   assert logs(10,3) == 0

#def test_finds_logs_when_a_is_exact_divisor():
 #   assert logs(4,64) == 3
