"""
10. ​Write a Python program to remove the characters
which have odd index values of a given string. 
"""

sample_str = 'Dingobingomingo.'
result = ''
for i in range(0,len(sample_str),2):
	result = result + sample_str[i]

print(result)
