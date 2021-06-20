import pytest

def add(x):
    return x + 1

def test_add():
    assert add(1) == 2

if __name__ == '__main__':
    pytest.main()