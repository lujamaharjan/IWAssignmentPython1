"""
8. ​Write a Python program to remove the
 n​th​ index character from a nonempty string.
"""

def remove_nth_char(my_str, index):
	result  = ""
	counter  = 0
	for i in my_str:
		if counter != index:
			result = result + i
		counter += 1

	return result

new_str = remove_nth_char("tiger", 2)
print(new_str)


