def positiveSum(arr):
    sum = 0
    for i in arr:
        if int(i) >= 0:
            sum += int(i)
    return sum

print(positiveSum([1, -4, '7', 12]))
print(positiveSum([-1, -2, -3, -4]))
print(positiveSum([]))
