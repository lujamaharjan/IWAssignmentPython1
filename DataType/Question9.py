"""
9. ​Write a Python program to change a 
given string to a new string where the 
first and last chars have been exchanged
"""

sample_str = "dog"
first_char = sample_str[0]
last_char = sample_str[-1]

result_str = last_char +sample_str[1:-1] + first_char


print(result_str)