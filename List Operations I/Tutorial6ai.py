number = [1,3,5,9,7,8,2,6,3,11]

try:
    i=int(input())
    if 0 < i <= int(len(number)):
        print(str(number[i-1]))
    else:
        print("Error: Invalid Input")
except:
    print("Error: Invalid Input")
