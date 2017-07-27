def permutation(word):
	if (len(word) <= 1):
		return [word]
	perms = permutation(word[1:])
	char = word[0]
	allPermutations = []
	for perm in perms:
		for i in range (len(perm)+1):
			allPermutations.append(perm[:i] + char + perm[i:])
	return allPermutations

print permutation("abc")