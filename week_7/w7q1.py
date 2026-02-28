# Armstrong number using while loop

num = int(input("Enter a number : "))

sum = 0
n = len(str(num))

for x in str(num):
    sum += int(x)**n

if sum == num:
    print("It's a Armstrong Number.")
else:
    print("It's not a Armstrong Number.")