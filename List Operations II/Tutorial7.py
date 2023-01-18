num=int(input())
list1=[]

while num>0:
    data=int(input())
    list1.append(data)
    num-=1


for i in range(0, 50):
    b=0
    if i in list1:
        b+=1
        c=list1.index(i)
        for j in range(c+1, len(list1)):
            if i==list1[j]:
                b+=1
        if b!=2:
            print(i)
    
