from calculator import addition, soustraction, division


def test_addition():
    assert addition(1, 2) == 3

def test_soustraction():
	assert soustraction(2,1) == 1

def test_division():
	assert division(6,2) == 3
