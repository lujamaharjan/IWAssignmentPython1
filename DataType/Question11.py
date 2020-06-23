"""
11. ​Write a Python program to count the 
occurrences of each word in a given sentence
"""

my_sen = 'she said she was eating a fruit'
word_list = my_sen.split(' ')

presented_word  = set(word_list) 

result = dict() 

for i in word_list:
	frequency = word_list.count(i)
	result[i] = frequency

print(result)