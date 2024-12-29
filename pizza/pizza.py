import sys
from tabulate import tabulate
import csv

def main():
    check_file_cmd()
    try:
        with open(f"{sys.argv[1]}", "r") as file:
            read = csv.DictReader(file)
            print(tabulate(read, headers = "keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("Not a CSV file")






def check_file_cmd():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()