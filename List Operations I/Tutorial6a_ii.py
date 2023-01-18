number = [1,3,5,9,7,8,2,6,3,11]

i=int(input())
try:
    a=number.index(i)
    print(str(a))
except:
    print(str(-1))
