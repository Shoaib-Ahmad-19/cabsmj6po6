# A document cleanup tool needs to normalize text copied from notes. 
# Write a Python program to remove indentation from each line of a multi-line text.
s = """
        This is line one.    
            This is line two.    
        This is line three.     
"""
lines = s.splitlines()
cleantxt = [line.lstrip() for line in lines]

res = "\n".join(cleantxt)
print(res)
