def disemvowel(string1):
    newstr = ""
    for char in string1:
        if char in 'a,e,i,o,u':
            newstr += ""
        else:
            newstr += char
    print newstr
disemvowel("aeiou")
