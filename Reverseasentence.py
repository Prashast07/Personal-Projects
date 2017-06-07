# To Reverse a sentence
def reverseWords(s):
	list1 = []
	s1 = s.split(" ")
	len1 = len(s1)
	for i in range(len1):
		s2 = s1[i][::-1]
		list1.append(s2)
	str1 = ' '.join(list1)
	print str1
reverseWords("Coding in Python")