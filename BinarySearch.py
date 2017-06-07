#Binary Search
def bsearch(alist,item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return bsearch(alist[:midpoint], item)
			else:
				return bsearch(alist[midpoint+1:],item)

testlist = [0,1,2,3,4,5,6,7]
print bsearch(testlist, 8)



