# Write a Python program that takes a month (1–12) and a year, uses a list of 
# days in each month, and prints the correct number of days. Make sure of leap 
# year for February.


m = int(input("Enter month number : "))

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
