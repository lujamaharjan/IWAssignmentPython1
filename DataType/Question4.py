"""
4.​ Write a Python program to get a single string 
from two given strings, separated by a space and
swap the first two characters of each string. 
Sample String : 'abc', 'xyz'  
Expected Result : 'xyc abz'
"""

first_str = 'abc'
second_str = 'xyz'

temp1 = first_str[0:2]
temp2 = first_str[2:len(first_str)]

temp3 = second_str[0:2]
temp4 = second_str[2: len(second_str)]

result = temp3 + temp2
result += ' '
result += temp1 + temp4

print(result)
