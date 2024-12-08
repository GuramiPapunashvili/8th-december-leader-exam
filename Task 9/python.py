def identifyPrimes(n1,n2):
    res = []
    def checkPrime(num):
        if num == 1:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    for i in range(n1,n2+1):
        if checkPrime(i):
            continue
        else:
            res.append(i)
    return res

print(identifyPrimes(10,20))
print(identifyPrimes(1,10))
print(identifyPrimes(20,30))
print(identifyPrimes(24,25))
print(identifyPrimes(1,1))

    