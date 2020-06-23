"""
3. ​Write a Python program to get a string 
from a given string where all occurrences 
of its first char have been changed to '$',
except the first char itself.  
Sample String : 'restart' 
Expected Result : 'resta$t' 
"""

sample_string = 'hahahaha'

string_without_first_char = sample_string[1:len(sample_string)]
result = string_without_first_char.replace(sample_string[0], '$')
print(result)
result = sample_string[0] + result
print(result)