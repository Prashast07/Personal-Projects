#Finding Min Value

def min(l):
	
	min = l[0]
	i = 1
	for i in range(len(l)):
		if l[i] < min:
			min = l[i]
			print i
	return min
print min([1,7,3,0,6,9])