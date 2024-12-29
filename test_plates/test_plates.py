from plates import is_valid

def main():
    test_len()
    test_letter()
    test_numbers()
    test_zero()
    test_alpha()
    test_twoletter()

def test_len():
    assert is_valid('AB') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCAKSJDB') == False

def test_letter():
    assert is_valid('12ABC') == False
    assert is_valid('A12BC') == False
    assert is_valid('ABC12') == True

def test_numbers():
    assert is_valid('ABD12') == True
    assert is_valid('AB12C') == False

def test_zero():
    assert is_valid('ACD01') == False
    assert is_valid('ACD10')== True

def test_alpha():
    assert is_valid('ABD_EF') == False
    assert is_valid('AB!21') == False
    assert is_valid('ABC DE') == False

def test_twoletter():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('22') == False


if __name__ == '__main__':
    main()