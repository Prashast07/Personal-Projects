def stringCompression(s):
	length = len(s)
	count = 1 
	compression = ""
	compression += s[0]
	for index in range(length -1):
		if s[index] == s[index+1]:
			count += 1
		else:
			if(count >= 1):
				compression += str(count)
			compression += s[index +1]
			count = 1
	if count >= 1:
		compression += str(count)
		 
	print compression

stringCompression("abbccccd")