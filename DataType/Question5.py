"""
5.​ Write a Python program to add 'ing' at 
the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc' 
Expected Result : 'abcing'  
Sample String : 'string' 
Expected Result : 'stringly'
"""

sample_string = 'johning'

result = ''
if len(sample_string) < 3:
	result = sample_string

else:
	if sample_string.endswith('ing'):
		result = sample_string + "ly"
	else:
		result = sample_string + 'ing'

print(result)

