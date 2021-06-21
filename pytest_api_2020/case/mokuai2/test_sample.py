import pytest


def add(x):
    return x + 1

def test_add():
    pytest.assume(add(2) == 3)
    pytest.assume(add(3) == 4)
    print("测试完成")

def test_add2():
    assert add(1) == 2

if __name__ == '__main__':
    pytest.main()