def rectArea(*r):
    return r[2]*r[3]

nOfRectangles=int(input())
sumOfRectangles=0
for i in range(nOfRectangles):
    dimensions=input().split()
    sumOfRectangles+=rectArea(int(dimensions[0]),int(dimensions[1]),int(dimensions[2]),int(dimensions[3]))
print(sumOfRectangles)