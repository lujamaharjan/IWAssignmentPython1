# 8.​ Write a Python function that takes a list and 
# returns a new list with unique elements of the first list. 
# Sample List : ​ [1,2,3,3,3,3,4,5] 
# Unique List :


def unique_elemented_list(myList):
	unique_list = []
	for i in myList:
		if i not in unique_list:
			unique_list.append(i)

	return unique_list


print(unique_elemented_list([1,2,3,3,3,3,3,4,5,5]))
