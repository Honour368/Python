# def isPrime(n):
#     for i in range(2, (n//2)+1):
#         if i>(n//2):
#             return True
#         if n%i==0:
#            return False
#         return True
# n=int(input())
# if isPrime(n):
#    print("true")
# else:
#    print("false")

def isPrime(n, i):
    if i>(n//2):    #that is, if the divisor is greater than half of n, then it can't be a factor. Hence, base case...once it gets to greater than half, it stops
        return True
    if n%i==0:
        return False
    return isPrime(n, i+1)

n=int(input())
if isPrime(n,2):
    print("true")
else:
    print("false")