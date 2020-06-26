# 16.​ Write a Python program to square and cube 
# every number in a given list of integers using Lambda

square = lambda n : n ** 2
cube =  lambda n: n ** 3


sample_list = [1, 2, 3, 4, 5, 6, 7]

squared_list = list(map(square, sample_list))
cubed_list = list(map(cube, sample_list))

print(squared_list)
print(cubed_list)