import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b",s,re.IGNORECASE)

    if match:
        a = match
        return len(a)
    else:
        return 0


if __name__ == "__main__":
    main()

# uzatmak icin bisey yaptik bakalim
