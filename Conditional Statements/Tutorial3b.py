a = int(input())
b = int(input())
c = int(input())

if (a+b)>c and (b+c)>a and (c+a)>b and a>0 and b>0 and c>0:
    if a==b==c:
        print("equilateral")
    elif a==b or b==c or a==c:
        print("isosceles")
    elif a!=b!=c:
        print("scalene")
else:
    print("impossible")
