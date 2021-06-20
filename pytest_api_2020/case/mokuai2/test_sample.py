import pytest
import pytest_assume

def add(x):
    return x + 1

def test_add():
    pytest.assume(add(2) == 2)
    pytest.assume(add(2) == 3)

def test_add2():
    pytest.assume(add(1) == 2)

if __name__ == '__main__':
    pytest.main(["-v","./test_sample.py"])