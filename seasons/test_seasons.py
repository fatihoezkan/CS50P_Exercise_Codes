from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("2020-01-01") == (2020,1,1)

if __name__ == "__main__":
    main()
