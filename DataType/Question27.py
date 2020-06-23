"""
26.​ Write a Python program to insert a given 
string at the beginning of all items in a list. 
Sample list : [1,2,3,4], string : emp 
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""

initial_list = [1,2,3,4,5,]
mix_str = 'a'

result = []
for item in initial_list:
	result.append(f'{mix_str}{item}')

print(result)