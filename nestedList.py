
def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item
flatten([1,2,3,[4,5,[7,4,5],6,7],10,11])