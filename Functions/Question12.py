# 12.​ Write a Python program to create a function that 
# takes one argument, and that argument will be multiplied 
# with an unknown given number.  
from random import randint

mul = lambda n: n * randint(1, 100)

print(mul(9))
