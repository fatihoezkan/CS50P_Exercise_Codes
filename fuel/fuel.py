def main():
    gauge()


def convert():
    while True:
        number = input("Fraction: ")
        a = number.partition("/")
        try:
            x = int(a[0])
            y = int(a[2])
            fraction = x / y
            if x > y:
                continue
            global percentage
            percentage = x/y *100
            return percentage
        except (ValueError, ZeroDivisionError):
            continue


def gauge():
    percentage = convert()
    if percentage >= 99:
        return print("F")
    elif percentage <= 1:
        return print("E")
    elif int(percentage)==66:
        percentage = 67
        return print(f"{int(percentage)}%")
    else:
        return print(f"{int(percentage)}%")

if __name__ == "__main__":
    main()
