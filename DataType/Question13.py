"""
13. ​Write a Python program that accepts a comma separated
 sequence of words as input and prints the unique 
 words in sorted form (alphanumerically).  
Sample Words : red, white, black, red, green, black 
Expected Result : black, green, red, white,red 
"""

user_input = input("Please enter comma separated words :: ")
word_list = user_input.split(", ")
word_list.sort()

result = ''
for word in word_list:
	result = result + word + ", "

print(result)
