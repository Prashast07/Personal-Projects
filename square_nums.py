def square_nums(num):
    list1 = []
    list2 =[]
    count = 0
    for i in range(1,num):
        list1.append(i)
    length = len(list1)
    for i in range(length):
        if list1[i] * list1[i] < num:
            list2.append(list1[i])
            count += 1
    print count
square_nums(25)