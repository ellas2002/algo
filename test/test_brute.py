from brute_string import str_match, str_find


def test_brute_for_position_of_pattern():
    assert str_match("abracadabra", "cad") == 4

def test_brute_for_position_of_patter():
    assert str_match("abracadabra", "abr") == 0

def test_brute_for_position_of_patten():
    assert str_find("abracadabra", "abr") == 0
    #assert matcher.__bruteforce('abr') == 0
