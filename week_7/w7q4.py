def GCD(x,y):
    if x <= 0 or y <= 0 :
        return -1
    else:
        while (y):
            x,y = y, x%y
        return x
    

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(f"The GCD of {a} and {b} using Euclidean algorithm is {GCD(a,b)}")