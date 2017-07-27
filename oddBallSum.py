def oddball_sum(numbers):
    length = len(numbers)
    summation = 0
    for i in range(length):
        if numbers[i] % 2 != 0:
            summation = summation + numbers[i]
    print summation
oddball_sum([0,6,4,4])