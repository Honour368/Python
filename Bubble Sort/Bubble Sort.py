def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]

a=[int(item) for item in input().split(" ")]
bubbleSort(a)
for i in a:
    print(i, end=(" "))