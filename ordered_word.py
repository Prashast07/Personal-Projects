def ordered_word(string1):
    maxSubString = ""
    temp = ""
    previousChar = ""
    for char in string1:
        if char >= previousChar:
            return True
        previousChar = char

print ordered_word("aabbddd")
