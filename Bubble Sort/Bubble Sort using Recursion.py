def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]

def bubbleSort_recursion(data, n):   #n is the length of data or last index in the list and represents how many times the function sorts the list
    if n<1:     #base case
        return (data)
    else:       
        for i in range (1, n):
            if data[i]<data[i-1]: 
                data[i], data[i-1]=data[i-1], data[i]
        bubbleSort_recursion(data, n-1)

a=[int(item) for item in input().split(" ")]
bubbleSort_recursion(a, len(a))
for i in a:
    print(i, end=(" "))