import sys

def main():
    check()
    try:
        f = open(f"{sys.argv[1]}" , "r")
        lines =f.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0
    for line in lines:
        if lines_check(line) == True:
            continue
        else:
            count += 1
    print(count)


def lines_check(line):
    if line.isspace():
        return True
    if line.lstrip()[0] == "#":
        return True
    return False

def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
