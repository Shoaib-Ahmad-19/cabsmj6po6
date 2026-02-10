# A text-filtering tool needs to remove noisy characters occurring at odd 
# positions. Write a Python program that takes a string and removes all 
# characters at even index values. 

s = input("Enter a String: ")
r =""
'''sdyc'''
for i in range(len(s)) :
    if not(i&1) :
        r +=s[i]

print(r)