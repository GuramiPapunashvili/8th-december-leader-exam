import math

def positiveFlooredSum(arr):
    res = 0
    for i in arr:
        if i >= 0:
            res += math.floor(i) 
    return res

print(positiveFlooredSum([1, -4, 7, 12])) 
print(positiveFlooredSum([-1.5, 2.7, -3.3, 4.8])) 
print(positiveFlooredSum([])) 
print(positiveFlooredSum([-1, -2, -3])) 

