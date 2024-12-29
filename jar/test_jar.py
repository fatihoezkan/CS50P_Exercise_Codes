
import pytest
from jar import Jar

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("invalid")

def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)  # Exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(-1)  # Negative value

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)  # Not enough cookies
    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Negative value

