# A billing system receives an unknown count of numeric entries per invoice. 
# Write a Python function that accepts arbitrary integers and returns their sum. 
# (Hint: use *args) 
sum = 0
while(True):
    a = int(input("Enter a Number: "))
    if a == 0 :
        break
    else:
        sum +=a
    
print(f"Total Sum : {sum}")