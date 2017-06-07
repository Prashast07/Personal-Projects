# Find Missing Number
def missing_number(l):
	length = len(l)
	sum1 = 0
	sum = ((length + 1) * (length + 2)) //2
	for i in range(length):
		sum1 = sum1 + l[i]
	missing_number = sum - sum1
	print missing_number
missing_number([1,2,3,4,5,6,8])