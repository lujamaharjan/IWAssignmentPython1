# 35.​ Write a Python program to iterate over dictionaries using for loops.

our_dic = {'apple':1, 'banana':4, 'coconut':7}

#gives key only
for key in our_dic:
	print(key, '=', our_dic[key])

#iteraties as tuple
for item in our_dic.items():
	print(item)

for key, value in our_dic.items():
	print(key, '=>', value)

for key in our_dic.keys():
	print(key)

for val in our_dic.values():
	print(val)