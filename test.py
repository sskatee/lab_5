import pytest

from master import triangle, simple, length_str, is_int
from sort import bubble_sort, selection_sort
from for_fixture import *

#проверка обычных функций
def test_triangle():
    assert triangle(12, 14, 10) == True


def test_simple():
    assert simple(5) == True
    assert simple(8) == False


def test_length_str():
    assert length_str('car') == 3
    assert length_str('system') == 6


def test_is_int():
    assert is_int(15) == True
    assert is_int('15') == False



#проверка простых функций для фикстур
@pytest.fixture()
def get_chet_num():
    print('\nРабота фикстуры')
    ch_n=[]
    for num in range(1, 11):
        if num%2==0:
            ch_n.append(num)
    yield ch_n
    print('\nРабота финализатора')

def test_sum_1(get_chet_num):
    x=get_chet_num
    assert sum_1(x) == [7,9,11,13,15]

def test_diff_1(get_chet_num):
    x = get_chet_num
    assert diff_1(x) == [-3,-1,1,3,5]

def test_prod_1(get_chet_num):
    x = get_chet_num
    assert prod_1(x) == [10,20,30,40,50]

#проверка сортировок
def test_bubble_sort():
    assert bubble_sort([11, 25, 333, 444, 21, 2, 5, 9, 178]) == [2, 5, 9, 11, 21, 25, 178, 333, 444]

def test_selection_sort():
    assert selection_sort([13,1345,24,2,36,7,86,3]) == [2, 3, 7, 13, 24, 36, 86, 1345]
