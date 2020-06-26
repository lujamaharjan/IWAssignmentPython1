# 6.​ Write a Python function to check whether a number is in a given range. 

def is_in_range(n, start, end):
	if n in range(start, end): 
		return True
	else:
		return False

x = is_in_range(n=8, start=1, end=9)
print(x)