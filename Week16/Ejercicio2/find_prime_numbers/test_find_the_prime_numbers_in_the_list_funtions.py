import pytest

from find_the_prime_numbers_in_the_list import prime_numbers

def test_prime_numbers_dont_work_with_letters():
    input_list = [1, 4, 6, 7, "A", 9, 67]
    with pytest.raises(TypeError):
        prime_numbers(input_list)


def test_prime_numbers_works_correctly():
    input_list = [1, 4, 6, 7, 13, 9, 67]
    result = prime_numbers(input_list)
    assert result == [7, 13, 67]


def test_prime_numbers_works_with_any_size_number():
    input_list = [1,4,67,10000019,566434355]
    result = prime_numbers(input_list)
    assert result == [67,10000019]
