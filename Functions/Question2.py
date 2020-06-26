# 2.​ Write a Python function to sum all the numbers in a list. 
# Sample List ​ : (8, 2, 3, 0, 7) 
# Expected Output ​ : 20

def sum_numbers(arg_list):
	return sum(arg_list)

total = sum_numbers([8, 2, 3, 0, 7])
print(total)