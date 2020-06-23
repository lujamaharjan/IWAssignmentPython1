'''
2.​ Write a Python program to get a string made of the 
first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, 
return instead of the empty string. 
Sample String : 'Python' 
Expected Result : 'Pyon' 
Sample String : 'Py' 
Expected Result : 'PyPy' 
Sample String : ' w' 
Expected Result : Empty String
'''

my_string = "python"
result = ''

if len(my_string) < 2 :
	pass
	
else:
	result += my_string[0:2]
	result += my_string[-2:len(my_string)]

print(result)