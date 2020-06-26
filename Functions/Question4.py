# 4.​ Write a Python program to reverse a string. 
# Sample String ​ : "1234abcd" 
# Expected Output ​ : "dcba4321"


def make_reverse(my_str):
	return my_str[::-1]

rev_str = make_reverse("1234abcd")
print(rev_str)