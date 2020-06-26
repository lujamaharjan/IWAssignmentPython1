# 15.​ Write a Python program to filter a list of integers using Lambda.  


int_list = list(filter(lambda x: isinstance(x, int), [1, 'a', 2, True, 'b', 4.5]))
print(int_list)