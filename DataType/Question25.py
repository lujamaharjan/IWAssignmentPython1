"""
25.​ Write a Python program to check whether
all dictionaries in a list are empty or not. 
Sample list : [{},{},{}] 
Return value : True 
Sample list : [{1,2},{},{}] 
Return value : False
"""

def isempty(dic):
	if len(dic) > 0:
		return False
	else:
		return True


sample_list = [{},{},{}]
allempty = True
for di in sample_list:
	if not isempty(di):
		allempty = False
		break
	
print(allempty)