import  bank

def main():
    test_hello()
    test_h()
    test_other()

def test_hello():
    assert bank.value('hello') == 0
    assert bank.value('Hello') == 0

def test_h():
    assert bank.value('hi') == 20
    assert bank.value('Hi') == 20

def test_other():
    assert bank.value('WWhatsupp') == 100
    assert bank.value('good morning') == 100

if __name__ == '__main__':
    main()