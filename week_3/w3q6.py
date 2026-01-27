# A robotics controller swaps sensor IDs efficiently. 
# Read two integers and exchange their values using the XOR(^) operator.

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

a = a ^ b
b = a ^ b
a = a ^ b

print(f"The values after swapping :\nFirst Number : {a}\nSecond Number : {b}")