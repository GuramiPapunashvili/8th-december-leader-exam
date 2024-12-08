def findMissingNumber(arr):
    if len(arr) == 1:
        return []
    for i in range(1,len(arr)):
        if i not in arr:
            return i

print(findMissingNumber([1, 2, 4, 5]))
print(findMissingNumber([3, 5, 6, 1, 2]))
print(findMissingNumber([2]))