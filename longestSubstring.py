s  = "azcbobobegghakl"
maxSubString = ""
temp = ""
previousChar = ""
for char in s:
    if char >= previousChar:
        temp += char
        if len(temp) > len(maxSubString):
            maxSubString = temp
    else: temp = char
    previousChar = char
print maxSubString