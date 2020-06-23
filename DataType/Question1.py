
'''
1.​ Write a Python program to count the number 
of characters (character frequency) in a string. 
Sample String : google.com' 
Expected Result : 
{'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

sample_string = 'google.com'

#filtering unique char
presented_char  = set(sample_string) 

result = dict() 

for i in presented_char:
	frequency = sample_string.count(i)
	result[i] = frequency

print(result)