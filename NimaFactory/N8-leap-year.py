print("N8-leap-year V1.0 running...\n")
print('enter a year and know about the year')
print('is the year, leap year?\n')
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 != 0 and year % 4 == 0:
        leap = True

    return leap

year = int(input('enter year number : '))
print(is_leap(year))