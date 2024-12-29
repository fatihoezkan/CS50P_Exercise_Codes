def main():
    fraction = input("Fraction: ")
    fraction_convert = convert(fraction)
    result = gauge(fraction_convert)
    print(result)


def convert(fraction):
    while True:
        a = fraction.partition("/")
        try:
            x = int(a[0])
            y = int(a[2])
            f  = x / y
            if f <= 1:
                percentage = int(f *100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
