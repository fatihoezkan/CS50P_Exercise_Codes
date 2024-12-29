from twttr import shorten



def main():
    test_shorten()
    test_numbers()
    test_punctuation()

def test_shorten():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('twitter') == 'twttr'

def test_numbers():
    assert shorten('1234') == '1234'

def test_punctuation():
    assert shorten('!?,') == '!?,'


if __name__ == "__main__":
    main()