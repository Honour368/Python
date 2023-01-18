num=int(input())
count=0
factor=True

if num<0:
    print("Error: Negative number")

else:
    for k in range(2, int(num), 1):
        if num%k==0:
            factor=True
            if factor:
                count+=1
    print(str(count))

