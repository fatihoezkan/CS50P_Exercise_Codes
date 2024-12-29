import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.search(r"^(1[0-9][0-9]|[0-9][0-9]|[0-9]|2[0-4][0-9]|25[0-5])\."
                      r"(1[0-9][0-9]|[0-9][0-9]|[0-9]|2[0-4][0-9]|25[0-5])\."
                      r"(1[0-9][0-9]|[0-9][0-9]|[0-9]|2[0-4][0-9]|25[0-5])\."
                      r"(1[0-9][0-9]|[0-9][0-9]|[0-9]|2[0-4][0-9]|25[0-5])$",ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
