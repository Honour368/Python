def rectArea(r0, r1, r2, r3):       #width*height
    return (r2-r0)*(r3-r1)

def getOverlap(r1, r2):    #overlap for two rectangles
        x1=min(max(r1[0], r1[2]), max(r2[0], r2[2]))
        y1=max(min(r1[1], r1[3]), min(r2[1], r2[3]))
        x2=max(min(r1[0], r1[2]), min(r2[0], r2[2]))
        y2=min(max(r1[1], r1[3]), max(r2[1], r2[3]))
        return (x1,y1,x2,y2)

nOfRectangles=int(input())
rectangle=[]
for i in range(nOfRectangles):
    dimensions=input().split()
    r=(int(dimensions[0]),int(dimensions[1]),(int(dimensions[2])+int(dimensions[0])),(int(dimensions[3])+int(dimensions[1])))
    rectangle.append(r)

maxX=0
maxY=0
for s in rectangle:
    for j in range(0,4,2):
        if s[j]>maxX:
            maxX=s[j]
    for k in range(1,4,2):
        if s[k]>maxY:
            maxY=s[k]
isTrue=True
for s in rectangle:
    if s[3]<1000:
        isTrue=True
    else:
        isTrue=False
if isTrue:
    list1 = [[0 for i in range(maxX)] for j in range(maxY)]       #note: the initial one used; create row, then append row to list1...causes multiple references to the zeros in list1
else:
    totalArea=0

for s in rectangle:
    if isTrue:
        for k in range(s[1], s[3]):    #columns    #repeats
            for j in range(s[0], s[2]):    #rows
                (list1[k][j])+=1  
    else:
        totalArea+=rectArea(*s)

if isTrue:
    areaSum=0
    for s in list1:
        for p in s:
            if p>0:
                areaSum+=1
    print(areaSum)
else:
    totalArea+=rectArea(*getOverlap(rectangle[0], rectangle[1]))
    print(totalArea)