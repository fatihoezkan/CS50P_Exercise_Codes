import csv, sys


def main():
    check()
    with open(f"{sys.argv[2]}", "w", newline='') as after_csv:
        headers= ["first","last","house"]
        writer = csv.DictWriter(after_csv, fieldnames=headers)
        writer.writeheader()
        with open("before.csv", "r") as before_csv:
            before = csv.DictReader(before_csv)
            for row in before:
                last , first = row["name"].split(",")
                last = last.strip()
                first = first.strip()
                house = row["house"]
                writer.writerow({"first": first , "last" : last, "house": house})


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    try:
        f= open(sys.argv[1])
    except:
        sys.exit(f"Could not {sys.argv[1]}")




if __name__ == "__main__":
    main()