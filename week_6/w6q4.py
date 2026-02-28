#  Write a program to print number of days in a month. (Chained Conditional)

m = int(input("Enter month number (0-12): "))

if m > 0 and m <= 12:
    if m in [1,3,5,7,8,10,12]:
        print("The number of days : 31")
    elif m in [4,6,9,11]:
        print("The number of days : 30")
    elif m == 2:
        year =int(input("Enter the year : "))
        if (year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("The number of days : 29")
        else:
            print("The number of days : 28")
else:
    print("There are only 12 months in a year.")