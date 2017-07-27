def luckySeven(numbers):
    length = len(numbers)
    for i in range(length - 2):
        list1 = numbers[i:i+3]
        if sum(list1) == 7:
            print "OK"


luckySeven([1,2,3,4,1,2])
