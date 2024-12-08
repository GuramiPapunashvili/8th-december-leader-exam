def threeSumProblem(arr):
    arr = sorted(arr)
    sum = 0
    res = []
    for i in range(len(arr)-2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right=len(arr)-1
        while right>left:
            sum += arr[i]
            sum += arr[left]
            sum +=arr [right]
            if sum == 0:
                res.append(arr[i])
                res.append(arr[left])
                res.append(arr[right])
                while left<right and arr[left] == arr[left+1]:
                    left += 1
                while right>left and arr[right] == arr[right-1]:
                    right -=1
                    left+=1
                    right-=1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return res

print(threeSumProblem([-1, 0, 1, 2, -1, -4])) #არ მუშაობს მარა ნახე რამდენი ვწერე რამე დამიწერეთ
print(threeSumProblem([0, 0, 0]))
print(threeSumProblem([1, 2, -2, -1]))
            



    
            

