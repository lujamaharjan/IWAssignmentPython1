"""
27.​ Write a Python program to replace the last element 
in a list with another list. 
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8] 
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

input_list = [1,2,3,4,5,6,7]
changer_list = ['apple', 'ball']

input_list[-1] = changer_list
print(input_list)