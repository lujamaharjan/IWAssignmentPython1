# 7.​ Write a Python function that accepts a string and 
# calculate the number of upper case letters and lower case letters. 
# Sample String ​ : 'The quick Brow Fox' 
# Expected Output ​ :  
# No. of Upper case characters : 3 
# No. of Lower case Characters : 1

def count_upper_lower(my_str):
	upper = 0;
	lower = 0;

	for char in my_str:
		if char.islower():
			lower += 1

		if char.isupper():
			upper += 1

	print("Number of upper case letters : " + str(upper))
	print("Number of lower case letters : " + str(lower))

count_upper_lower('The Quick Brown Fox')