#22. ​Write a Python program to remove duplicates from a list.  

my_list = [1, 2, 4, 5, 6, 7, 1, 5, 1, 2]

result = []

for i in my_list:
	if i not in result:
		result.append(i)

print(result)