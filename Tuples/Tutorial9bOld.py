def rectArea(*r):       #width*height
    return (r[2]-r[0])*(r[3]-r[1])

def getOverlap(r1, r2):    #overlap for two rectangles
        x1=min(max(r1[0], r1[2]), max(r2[0], r2[2]))
        y1=max(min(r1[1], r1[3]), min(r2[1], r2[3]))
        x2=max(min(r1[0], r1[2]), min(r2[0], r2[2]))
        y2=min(max(r1[1], r1[3]), max(r2[1], r2[3]))
        return (x1,y1,x2,y2)

def overlapArea():
        for i in listRectangles:
                n=listRectangles[i]+1
                while n<len(listRectangles):
                        overlap1+=rectArea(getOverlap(i, listRectangles[n]))
                        n+=1

nOfRectangles=int(input())
sumOfRectangles=0
listRectangles=[]

for i in range(nOfRectangles):
        dimensions=input().split()  
        r=tuple(int(dimensions[0]),int(dimensions[1]),(int(dimensions[2])+int(dimensions[0])),(int(dimensions[3])+int(dimensions[1]))) #tupple containing x1,y1,x2,y2 created here
        listRectangles.append(r)
overlap1=0
for i in listRectangles:
        n=listRectangles[i]+1
        while n<len(listRectangles):
                overlap1+=rectArea(getOverlap(i, listRectangles[n]))
                n+=1


totalArea=0