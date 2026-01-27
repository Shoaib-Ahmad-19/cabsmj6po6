# A game console optimizes score calculation. Multiply a number by 10 using bitwise opoerators


n = int(input("Enter the number: "))

print(f"The result after Multiplying it by 10 is : {(n << 3)+ (n << 1)}")