#   A text-analysis tool needs statistics from a sentence. Write a Python function 
#   that accepts a string and counts the number of uppercase and lowercase letters 
#   using isupper(), islower(), upper(), lower(). 

def count(str):
    uppercase, lowercase = 0,0
    for i in str:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    
    print(f"UPPERCASE : {uppercase}\t LOWERCASE : {lowercase}")
            
str = input("Enter a String : ")
count(str)