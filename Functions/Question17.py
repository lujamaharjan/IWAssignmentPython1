# 17.​ Write a Python program to find if a given
#  string starts with a given character using Lambda.


starts_with = lambda test_str, test_char: test_str[0] == test_char

print(starts_with('apple', 'a'))
print(starts_with('apple', 'b'))