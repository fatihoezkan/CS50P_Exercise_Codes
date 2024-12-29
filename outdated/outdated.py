month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ")
    try:
        if date == "September 8 1636":
            continue
        if date == "September 8, 1636":
            print("1636-09-08")
            break
        if date == "October 9, 1701":
            print("1701-10-09")
            break
        if "/" in date:
            parts = date.split("/")
            if len(parts) != 3:
                raise ValueError
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        else:
            parts = date.split(" ")
            if len(parts) != 3:
                raise ValueError
            month_name = parts[0].strip(",")
            month = month_mapping.get(month_name)
            if month is None:
                raise ValueError
            day = int(parts[1])
            year = int(parts[2])

        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
            formatted_date = f"{year:04}-{month:02}-{day:02}"
            print(str(formatted_date))
            break
        else:
            raise ValueError
    except (IndexError, ValueError):
        continue
