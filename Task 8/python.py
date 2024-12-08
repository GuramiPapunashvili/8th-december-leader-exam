def longestSec(arr):
    arr = set(arr)
    length = 1
    num = 0
    for i in arr:
        if (i-1) not in arr:
            num = i
        while (num + 1) in arr:
            length += 1
            num += 1
    return length

print(longestSec([100, 4, 200, 1, 3, 2]))
print(longestSec([0, 0]))
print(longestSec([9, 1, 4, 7, 3, 2, 8, 5, 6]))

    

