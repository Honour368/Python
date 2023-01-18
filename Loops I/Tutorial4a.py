num=int(input())
factor=True

if num<0:
    print("Error: Negative number")

else:
    for k in range(2, int(num), 1):
        if num%k==0:
            factor=True
            if factor:
                print(str(k), end=" ")
            
    
    

#remainder should be zero
#
