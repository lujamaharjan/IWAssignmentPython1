# 45.​ Write a Python program to find the index of an item of a tuple. 


def findIndex(tup, item):
	count = 0 
	for i in tup:
		if i == item:
			return count
			brea
		count = count + 1


index = findIndex((1, 2, 4, 5, 6), 6)
print(index)

#inbuild method
print((1,3,2,4,5,6).index(4))