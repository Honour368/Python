pattern = str(input())
size = int(input())

def printPatternA(size):
    for i in range(1, size+1, 1):
        if i==1 or i==(size):
            for j in range(1, size+1, 1):
                print("#", end=(''))
            print("")
        else:
            for j in range(1, size+1, 1):
                if j==1 or j==(size):
                    print("#", end=(''))
                else:
                    print(" ", end=(''))
            print("")

def printPatternB(size):
     for i in range(1, size+1, 1):
        if i==1 or i==(size):
            for j in range(1, size+1, 1):
                print("#", end=(""))
            print("")
        else:
            for j in range(1, size+1, 1):
                if i==j:
                    print("#", end=(""))
                else:
                    print(" ", end=(""))
            print("")

def printPatternC(size):
     for i in range(1, size+1, 1):
        if i==1 or i==(size):
            for j in range(1, size+1, 1):
                print("#", end=(""))
            print("")
        else:
            for j in range(1, size+1, 1):
                if j==((size+1)-i):
                    print("#", end=(''))
                else:
                    print(" ", end=(''))
            print("")

def printPatternD(size):
     for i in range(1, size+1, 1):
        if i==1 or i==(size):
            for j in range(1, size+1, 1):
                print("#", end=(''))
            print("")
        else:
            for j in range(1, size+1, 1):
                if i==j or j==((size+1)-i):
                    print("#", end=(''))
                else:
                    print(" ", end=(''))
            print("")

           
if pattern == "a":
    printPatternA(size)
if pattern == "b":
    printPatternB(size)
if pattern == "c":
    printPatternC(size)
if pattern == "d":
    printPatternD(size)