# Max Repetion in a list
def max_repetition_with_hash(A):
	table = {}
	max = 0
	for element in A:
		if element in table:
			table[element] += 1
		elif element != "":
			table[element] = 1
		else:
			table[element] = 0
	for i in range(len(table)):
		if table.values()[i] > max:
			max = table.values()[i]
			maxRepeatedElement = table.keys()[i]
	print maxRepeatedElement
	print max

max_repetition_with_hash([1,2,2,2,3,3,3,3,3,5,5])

