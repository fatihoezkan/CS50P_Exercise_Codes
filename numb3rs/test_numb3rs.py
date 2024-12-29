import numb3rs
import sys

def main():
    test_case1()
    test_case2()
    test_case3()
    test_case4()


def test_case1():
    case1 = "255.255.255.255"
    assert numb3rs.validate(case1) == True

def test_case2():
    case2 = "cat"
    assert numb3rs.validate(case2) == False


def test_case3():
    case3 = "1.1.1.255"
    assert numb3rs.validate(case3) == True

def test_case4():
    case4 = "1.2.3.4.5"
    assert numb3rs.validate(case4) == False

def test_range():
    assert numb3rs.validate("20.260.15.35") is False



if __name__ == "__main__":
    main()