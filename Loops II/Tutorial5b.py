def isPerfect(number):
    factorSum=0
    for i in range(1, j, 1):
        if j%i==0:
            factor=i
        else:
            factor=0
        factorSum+=factor
    return factorSum

upperBound=int(input())

for j in range(1, (upperBound+1), 1):
    a=isPerfect(j)
    if a==j:
        print(str(a), end=" ")



