# A simple analytics module must calculate keyword frequency in user feedback. 
# Write a Python program to count occurrences of each word in a sentence.
from collections import Counter

s = input("Enter a String : ")
words = s.lower().split()
count = Counter(words)

print(count)
