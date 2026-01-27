#write a program to add two number without using arithmetic operators,  using bitwise operators

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

sum = a^b
carry = (a&b) << 1

sum += carry

print(f"The sum is {sum}")