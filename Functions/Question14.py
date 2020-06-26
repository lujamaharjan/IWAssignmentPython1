# 14.​ Write a Python program to sort a list of dictionaries using Lambd


sample_list = [{'weight': 5}, {'weight': 20}, {'weight': 12}]

sorted_list = sorted(sample_list, key = lambda dic: dic['weight'])
print(sorted_list)