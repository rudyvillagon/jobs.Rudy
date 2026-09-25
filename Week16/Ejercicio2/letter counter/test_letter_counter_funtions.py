import pytest

from letter_counter import letter_counter

def test_letter_counter_only_counts_letters():
    input = "This is Test Number 1234" 
    result = letter_counter(input)
    assert result == (3,13)


def test_letter_counter_works_good():
    input = "This is Test Number"
    result = letter_counter(input)
    assert result == (3,13)


def test_letter_counter_only_works_with_Str():
    input = [1234]
    with pytest.raises(AttributeError):
        letter_counter(input)
