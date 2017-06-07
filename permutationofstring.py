def isAPermutation(a_string, b_string):
	if len(a_string) != len(b_string): 
		print "Not a Permutation"
	if sorted(a_string) == sorted(b_string): 
		print "Is a Permutation"
	else:
		print "Not a permutation"
isAPermutation("prashast", "rashasqp")