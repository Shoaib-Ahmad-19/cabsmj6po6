#  A sensor module collects readings from three temperature probes. 
# Write a program to determine the lowest reading using if–else logic.


a =int(input("Enter first reading :"))
b =int(input("Enter second reading :"))
c =int(input("Enter third reading :"))

if a<b :
    if a<c:
        print(f"{a} is lowest temperature reading..")
    else:
        print(f"{c} is lowest temperature reading..")
else:
    if b<c:
        print(f"{b} is lowest temperature reading..")
    else:
        print(f"{c} is lowest temperature reading..")