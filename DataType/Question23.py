#Write a Python program to check a list is empty or not.

def isempty(my_list):
	if len(my_list) > 0:
		return False
	else:
		return True

check_empty = isempty([])
check_empty1 = isempty([1,3,4])

print(check_empty)
print(check_empty1)