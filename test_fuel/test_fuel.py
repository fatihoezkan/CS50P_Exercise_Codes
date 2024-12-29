from fuel import gauge,convert
import pytest

def main():
    test_fullempty()
    test_input()


def test_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("aAS/DSA")


def test_fullempty():
    assert gauge(1/1) == "E"
    assert gauge(100) == "F"

if __name__ == "__main__":
    main()