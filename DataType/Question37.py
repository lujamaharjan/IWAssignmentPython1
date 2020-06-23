# 37.​ Write a Python program to multiply all the items in a dictionary.


my_dic = {'apple': 1, 'ball': 4, 'cat': 5}

product = 1
for val in my_dic.values():
	product  = product * val

print(product)