import pytest
import pytest_assume

def add(x):
    return x + 1

def test_add():
    pytest.assume(add(2) == 2)
    pytest.assume(add(3) == 2)
    print("测试完成")

def test_add2():
    assert add(1) == 2

if __name__ == '__main__':
    pytest.main()