"""
15.​ Write a Python function to insert a string in the middle of a string.  
Sample function and result :  
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
import math
def insert_in_middle(str1, str2):
	mid_index = math.ceil(len(str1)/2)
	return str1[0:mid_index] + str2 + str1[mid_index:len(str1)]

result = insert_in_middle("raar", 'd')
print(result)