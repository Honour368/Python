length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]

def RodCut(price, n):
    if n==0:
        return 0
    maxValue=0
    for 