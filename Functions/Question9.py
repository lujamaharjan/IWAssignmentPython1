"""
9.​ Write a Python function that takes a
number as a parameter and check the number is prime or not. 
Note : A prime number (or a prime) is a natural number greater
than 1 and that has no positive divisors other than 1 and itself. 
"""

def isprime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True


print(isprime(7))
print(isprime(8))
print(isprime(29))
print(isprime(99))

