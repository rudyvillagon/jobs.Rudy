import pytest

from Sum_Numbers import sum_numbers

def test_sum_numbers_only_works_with_numbers():
    list_input = [12,"A",14,65]
    with pytest.raises(TypeError):
        sum_numbers(list_input) 


def test_sum_numbers_works_good():
    list_input = [12,9,14,65]
    result = sum_numbers(list_input)
    assert result == 100 


def test_sum_numbers_only_works_list():
    list_input = "Dont Work"
    with pytest.raises(TypeError):
        sum_numbers(list_input) 

