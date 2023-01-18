num=int(input())
factorSum=0

for i in range(1, num, 1):
    if num%i==0:
        factor=i
    else:
        factor=0
    factorSum+=factor

print(str(factorSum))
