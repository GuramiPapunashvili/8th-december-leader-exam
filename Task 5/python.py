def checkAnagrams(s1,s2):
    arr = [i for i in s1]
    for i in s2:
        if i in arr:
            arr.remove(i)
        else:
            return False
    return len(arr) == 0

print(checkAnagrams("listen", "silent"))
print(checkAnagrams("hello", "world"))
print(checkAnagrams("triangle", "integral"))