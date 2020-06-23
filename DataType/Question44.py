# 44.​ Write a Python program to slice a tuple.

def slice_tuple(tup, start, end):
	temp = list(tup)
	temp = temp[start: end]
	return tuple(temp)

tup = ['ap','b', 'c', 'd', 'e']
sliced_tuple = slice_tuple(tup,1,5)
print(sliced_tuple)
