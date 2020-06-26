# 3.​ Write a Python function to multiply all the numbers in a list.  
# Sample List ​ : (8, 2, 3, -1, 7) 
# Expected Output ​ : -336 

def mul(my_list):
	product = 1
	for i in my_list:
		product *= i

	return product

print(mul([8,2,3,-1,7]))