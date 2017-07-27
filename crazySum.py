def crazy_sum(numbers):
    length = len(numbers)
    sum = 0
    for i in range(length):
        sum = sum + numbers[i] * i
    print sum

crazy_sum([2, 3, 5])