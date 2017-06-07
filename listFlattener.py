def flatten(S):
	if S == []:
		return S
	if isinstance(S[0], list):
		return flatten(S[0]) + flatten(S[1:])
	else:
		return S[:1] + flatten(S[1:])

print flatten([1,2,3,[4,5,6,[7,8],9],10,11])