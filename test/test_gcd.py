from gcd import gcd #from other file gcd import gcd

def test_finds_gcd_when_a_less():
    assert gcd(10,16) == 2

def test_finds_gcd_when_a_greater():
    assert_gcd(10,12) == 4

def test_finds_gcd_when_a_equal():
    assert_gcd(4,16) == 4