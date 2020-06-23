# 36.​ Write a Python program to sum all the items in a dictionary. 

my_dic = {'apple': 1, 'ball': 4, 'cat': 5}

total = 0
for val in my_dic.values():
	total  = total + val

print(total)