"""
6.​ Write a Python program to find the first appearance of 
the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string.  
Sample String : 'The lyrics is not that poor!' 
'The lyrics is poor!' 
Expected Result : 'The lyrics is good!' 
'The lyrics is poor!'

"""

sample_string = 'The lyrics is not that poor!'

not_index = sample_string.find('not')
poor_index = sample_string.find('poor')

str_length = len(sample_string)
result = ''

if not_index >= 0 and poor_index >= 0:
	if not_index < poor_index:
		result = sample_string[0: not_index]  
		result += "good" 
		result += sample_string[poor_index + 4: str_length]

print(result)