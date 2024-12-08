def findIntersections(arr,arr2):
    res = []
    for i in arr:
        if i in arr2:
            res.append(i)
    res = set(res)
    return list(res)

print(findIntersections([1, 2, 3], [2, 3, 4]))
print(findIntersections([1, 1, 2], [1, 3]))
print(findIntersections([], [1, 2]))
        