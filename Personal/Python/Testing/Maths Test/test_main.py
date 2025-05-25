from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_divide():
    with pytest.raises(ValueError, match= "Cannot divide by zero"):
        divide(1, 0)