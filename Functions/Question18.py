# 18.​ Write a Python program to check whether a 
# given string is number or not using Lambda.

check_num = lambda n : n.isnumeric()


print(check_num('123'))
print(check_num('abc'))