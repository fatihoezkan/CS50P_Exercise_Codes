from datetime import date
import re
import sys
import inflect
p= inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    year , month , day = check_birthday(birth_date)
    date_of_birth = date(year,month,day)
    # print(date_of_birth)
    date_of_today=date.today()

    #now we need to substract them...

    difference = date_of_today - date_of_birth
    # print(difference)
    total_minutes = difference.days * 24 *60
    # print(total_minutes)

    #you need write minutes not with numbers with words.
    # there is new module
    # method numbet_to_words
    minutes_words = p.number_to_words(total_minutes, andword = "")
    print(minutes_words.capitalize()+ " minutes")


def check_birthday(birth_date):
    a=re.search('^[0-9]{4}-[0-9]{2}-[0-9]{2}$',birth_date)
    if not a:
        sys.exit("Invalid Date")
    year, month, day =birth_date.split("-")
    return int(year), int(month), int(day)

if __name__ == "__main__":
    main()
