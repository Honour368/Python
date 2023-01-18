def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]

n=int(input())
list1=[]
for i in range(n):
    t=tuple(int(item) for item in input().split(" "))
    list1.append(t)
bubbleSort(list1)
for i in list1:
    for j in i:
        print(j, end=(" "))
    print()