#
#       ---------(x2,y2)
#       |       |
#       |     |-|-------| (x4,y4)
#       ---------       |
#   (x1,y1)   |         |         
#             -----------
#           (x3,y3)
X1=0
Y1=1
X2=2
Y2=3
def rectArea(r):
    if r[Y2]-r[Y1]>0 and r[X2]-r[X1]>0:
        return (r[Y2]-r[Y1])*(r[X2]-r[X1])
    return -1

def olRect(r1, r2):
    xa=max(r1[X1],r2[X1])
    ya=max(r1[Y1],r2[Y1])
    xb=min(r1[X2],r2[X2])
    yb=min(r1[Y2],r2[Y2])
    r=xa,ya,xb,yb
    #print("test:"+str(r1)+"-"+str(r2)+" overlap:"+str(r))
    if rectArea(r)>0:
        return [r]

    return []
    
    
def getOverlap(rList):
    
    totalArea=0
    for i in range(len(rList)):
        oList=[]
        area=0
        for j in range(i+1, len(rList)):
            r=olRect(rList[i],rList[j])
            if len(r)>0:
                oa=rectArea(r[0])
            
                oList.append(r[0])
                area+=oa
        if len(oList)>0:
           # print(f"o list:{oList}")
            ooa=getOverlap(oList)
            area-=ooa
        totalArea+=area
        
    return totalArea

r1=2,2,6,6
r2=5,3,7,5
r3=4,4,8,8
l=getOverlap([r1,r2,r3])
totalArea=rectArea(r1)+rectArea(r2)+rectArea(r3)-l
print(totalArea)
        
