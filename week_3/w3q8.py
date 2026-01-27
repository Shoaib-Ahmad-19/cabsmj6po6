#  A data-logging device swaps configuration settings. Read two integers and 
# exchange their values using addition and subtraction (avoid using a third variable)


a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

a = a + b
b = a - b
a = a - b

print(f"The values after swapping :\nFirst Number : {a}\nSecond Number : {b}")