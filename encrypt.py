def encrypt(string1):
    length = len(string1)
    count = 1
    compression = ""
    compression += string1[0]
    for index in range(length - 1):
        if string1[index] == string1[index + 1]:
            count += 1
        else:
            if (count >= 1):
                compression += str(count)
            compression += string1[index + 1]
            count = 1
    if count >= 1:
        compression += str(count)

    print compression

    length1 = len(compression)
    print length1
    ans = [[compression[i], compression[i+1]] for i in range(0,length1,2)]
    print ans

encrypt("aaabbcbbaaa")