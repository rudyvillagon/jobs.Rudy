import pytest

from reversed_words import Backwords

def test_backwords_only_works_with_Str():
    list_input = 1245
    with pytest.raises(TypeError):
        Backwords(list_input) 


def test_backwords_works_correctly():
    list_input = "This is a Test"
    result = Backwords(list_input)
    assert result == "tseT a si sihT"


def test_backwords_works_with_numbers_in_a_Str():
    list_input = "1234 This is a Test"
    result = Backwords(list_input)
    assert result == "tseT a si sihT 4321"