import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    start_url = re.search(r"youtube.com/embed/",s)
    if not start_url:
        return None
    end_url = re.search(r"((></iframe>)|( title=))",s)
    if not end_url:
        return None
    return "https://youtu.be/"+s[start_url.end() : end_url.start()-1]




if __name__ == "__main__":
    main()
