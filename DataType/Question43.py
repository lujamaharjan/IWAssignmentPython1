# 43.​ Write a Python program to remove an item from a tuple

def remove_item_from_tuple(tup, item):
	temp = []
	for i in tup:
		if i != item:
			temp.append(i)
	return tuple(temp)

my_tuple = (1,2,3,4,5)
new_tuple = remove_item_from_tuple(my_tuple, 3)
print(new_tuple)