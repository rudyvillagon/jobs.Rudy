
import pytest
from Bubble_Sort import Bubble_Sort


def test_bubble_sort_works_with_small_lists():
    # AAA
    # Arrange
    list_input = [90,1,23,56]
    # Act
    result = Bubble_Sort(list_input)
    # Assert
    assert result == [1,23,56,90]


def test_bubble_sort_works_with_big_list():
    # AAA 
    # Arrange
    list_input = [847, 126, 593, 711, 924, 34, 812, 458, 263, 379, 802, 651, 298, 57, 13, 932, 104, 765, 183, 591, 321, 84, 243, 975, 506, 767, 888, 649, 373, 118, 703, 433, 689, 255, 47, 610, 830, 326, 77, 197, 909, 466, 604, 347, 741, 173, 966, 314, 628, 352, 905, 744, 279, 517, 686, 422, 338, 45, 754, 86, 800, 139, 394, 232, 991, 665, 144, 501, 91, 722, 333, 216, 175, 108, 699, 606, 928, 129, 842, 71, 519, 156, 201, 583, 323, 949, 384, 689, 999, 612, 420, 536, 159, 281, 763, 14, 473, 613, 264, 198, 615, 743, 357, 356, 944, 162, 284, 511, 250, 789]
    # Act
    result = Bubble_Sort(list_input)
    # Assert
    assert result == sorted(list_input)

def test_bubble_sort_with_empty_list():
    # AAA
    # Arrange
    list_input = []
    # Act
    result = Bubble_Sort(list_input)
    # Assert
    assert result == []


def test_bubble_sort_only_works_with_list():    
    
    list_input = "Hola Mundo"

    with pytest.raises(TypeError):
        Bubble_Sort(list_input)

