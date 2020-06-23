"""
7. ​Write a Python function that takes a list of
words and returns the length of the longest one
"""

def long_string(args):
	longest = args[0]
	for i in range(len(args)):
		if len(longest) < len(args[i]):
			longest = args[i]

	return longest



long = long_string(['apple', 'ball', 'cat', 'dog', 'elephant'])
print(long)



