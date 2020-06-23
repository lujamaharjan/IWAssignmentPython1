"""
30.​ Write a Python script to check whether 
a given key already exists in a dictionary.
"""
def iskey_in_dict(dic, key):
	if key in dic.keys():
		return True
	return False

my_dic = {'name':'sachin', 'town':'lalitpur', 'country':'Nepal'}
key = 'name'

print(iskey_in_dict(my_dic, key))

