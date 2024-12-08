def editDistance(s1,s2):
    operations = 0
    arr1 = [i for i in s2]
    for i in s1:
        if i not in arr1:
            operations += s1.count(i)
            s1.replace(i,'')
    for i in range(len(s1)):
        if s1[i] != arr1[i]:
            operations += 1
            s1.replace(s1[i],arr1[i])
    return operations


print(editDistance("horse", "ros"))
print(editDistance("intention", "execution"))
print(editDistance("kitten", "sitting"))
