a = int(input("Enter First Value :"))
o = int(input("Choose Operatin :\n1 : Addition\n2 : Subtraction\n3 : Multiplication\n4 : Division \n5 : Modulus\n"))
b = int(input("Enter Second Value :"))

match o:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print(a%b)
    case _:
        print("Invalid Input")


print("Welcome to the National Art Museum\nDigital exhibits were introduced in 2015")