# 20.​ Write a Python program to find intersection of two given arrays using Lambda. 



first = ['a', 2, 3, 5, 7, 8, 9, 10]
second = ['b', 2, 4, 8, 9]

result = list(filter(lambda x: x in first, second)) 
print ("Intersection of two arrays: ",result)