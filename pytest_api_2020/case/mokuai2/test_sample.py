import pytest

def add(x):
    return x + 1

def test_add():
    assert add(1) == 2
    assert add(2) == 1

if __name__ == '__main__':
    pytest.main()