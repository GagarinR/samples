d = [('ksw', 0), ('ksw', 2), ('ksw', 5), ('kof', 1), ('kof', 4), ('ksw', 0), ('ksw', 2), ('ksw', 5), ('izu', 3), ('izu', 6), ('kof', 1), ('kof', 4), ('ksw', 0), ('ksw', 2), ('ksw', 5), ('izu', 3), ('izu', 6)]
# print(dict(d))
def sum_keys(lst):
	result = {}
	for item in lst:
		print("before adding", result)
		print(item[0], item[1])
		result[item[0]] = result.get(item[0], 0) + item[1]
		print("after adding", result)
		print('==='*2)
		
	print (result)

sum_keys(d)