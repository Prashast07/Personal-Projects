s = "bobhdhaboblklbobbob"

count = 0
subString = ""
for i in range(len(s)):
    if s[i] == 'b':
        subString = s[i:i+3]
        if subString == "bob":
            count += 1
print count
