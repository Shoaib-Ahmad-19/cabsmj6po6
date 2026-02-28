#  Palindrome


''' My Logic'''

def ispalindrome(s):
    return (s[:len(s)//2] == s[(len(s)//2) +1 if len(s)&1 else 0 :][::-1])
    

s = input("Enter the string :")

print(s[:len(s)//2])
print(s[len(s)//2 +1 if len(s)&1 else 0 :][::-1])

if ispalindrome(s):
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")


''' Standard method''' 

if s == s[::-1]:
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")
    
    