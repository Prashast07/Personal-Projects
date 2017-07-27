# n = size of array1
# m = size of array2
def merge(array1, array2, n, m):
    x = 0
    y = 0
    result = []
    k = 0

    while (x < n) and (y < m):
        if array1[x] > array2[y]:
            result.append(array1[x])
            x += 1
        else:
            result.append(array2[y])
            y += 1
    while x < n:
        result.append(array1[x])
        x += 1

    while y < m:
        result.append(array2[y])
        y += 1

    for i in result:
        print (i, end=" ")
        print("")