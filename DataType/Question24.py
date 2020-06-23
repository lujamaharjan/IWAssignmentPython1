#Write a Python program to clone or copy a list

first_list = [1, 'apple', True]
second_list = first_list.copy()
print(second_list)
print(first_list)
print(id(first_list))
print(id(second_list))