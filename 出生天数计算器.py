#Firstly,we should define a function which will point out the next day of the day we input.
def nextday(year, month, day):
    if day < daysinmonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

#Then,we must confirm the date order is the right order.
def dateisbefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

#After that, we should make a list which can return the day in month.
def daysinmonth(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if isleapyear(year):
            return 29
        return 28
    return 31

#Besides,we must know if the year you input is leap year or not.
def isleapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

#In the end, we can define the main function of the calculator.
def daysbetweendates(year1, month1, day1, year2, month2, day2):
    assert not dateisbefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateisbefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextday(year1, month1, day1)
        days += 1
    return days



if __name__ == '__main__':
    daysbetweendates(year1, month1, day1, year2, month2, day2)
#REMBER:please input the first date and the second date in order.
