def crazy_nums(num):
    list1 = []
    list2 = []
    list3 = []
    for i in range(1,num):
        list1.append(i)
    length = len(list1)
    for i in range(length):
        if list1[i] % 3 == 0 or list1[i] % 5 == 0 :
            list2.append(list1[i])
    length1 = len(list2)
    for i in range(length1):
        if list2[i] % 15 != 0:
            list3.append(list2[i])
    print list3

crazy_nums(20)
