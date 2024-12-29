import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    match = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) ([AP]M) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s)


    if match:
        grps = match.groups()
        if int(grps[1]) > 12 or int(grps[5]) > 12:
            #raise ValueError
            sys.exit(ValueError)
        time1 = new_time(grps[1],grps[2],grps[3])
        time2 = new_time(grps[5],grps[6],grps[7])

        return f"{time1} to {time2}"

    else:
        #raise ValueError
        sys.exit(ValueError)

def new_time(hour, minute, am_pm):
    if am_pm == "PM":
        new_hour = int(hour) + 12
        if new_hour == 24:
             new_hour = "12"
    else:
        new_hour = int(hour)
        if new_hour == 12:
            new_hour = "00"


    if minute == None:
        new_minute = "00"
        return f"{new_hour:02}:" + new_minute
    else:
        return f"{new_hour:02}:" + minute

#'9:00 AM to 5:00 PM'
#9 AM to 5 PM


if __name__ == "__main__":
    main()
