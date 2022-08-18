def date_input():
    day = int(input("enter a day : "))
    if day > 31:
        print("day cannot be more than 31")
        raise ValueError("run again N2-date-input and be careful")
    elif day < 1:
        print("day cannot be lower than 1")
        raise ValueError("run again N2-date-input and be careful")
    month = int(input("enter a month : "))
    if month > 12:
        print("month cannot be more than 12")
        raise ValueError("run again N2-date-input and be careful")
    elif month < 1:
        print("month cannot be lower than 1")
        raise ValueError("run again N2-date-input and be careful")
    year = int(input("enter a year : "))
    if year > 10000:
        print("you enter a year more than 10000")
    elif year < 0:
        print("year cannot be lower than 0")
        raise ValueError("run again N2-date-input and be careful")
    print(f"{year}/{month}/{day}")


print("N2-date-input V1.1 running\n")
date_input()
