import sys
sys.stdin=open('storage_input.txt')

N=int(input())

stor=[]

def maxheight(tuples):
    mh=0
    mhi=0
    for tuple in tuples:
        if tuple[1]>mh:
            mh=tuple[1]
            mhi=tuple[0]
    
    return (mhi,mh)

for _ in range(N):
    a,b=map(int,input().split())
    stor.append((a,b))

stor=sorted(stor)
h=maxheight(stor)
fullarea=((max(stor)[0]+1)-min(stor)[0])*h[1]

start=maxheight(stor)


for idx,el in enumerate(stor):
    stor[idx]=[idx,el]
    


alstor=sorted(stor, key = lambda x:x[1][1])
maxidx=alstor[-1][0]

def rightarea(lst,maxidx,start,rarea):
    maxh=0
    for idx in range(maxidx+1,len(stor)):
        if lst[idx][1][1]>=maxh:
            maxi=idx
            maxh=lst[idx][1][1]
    
    if maxi==len(stor)-1:
        k=rarea+(start[1]-maxh)*(stor[maxi][1][0]-stor[maxidx][1][0])
        return k

    else:
        k=rarea+(start[1]-maxh)*(stor[maxi][1][0]-stor[maxidx][1][0])
        return rightarea(lst,maxi,start,k)

def leftarea(lst,maxidx,start,larea):
    maxh=0
    for idx in range(0,maxidx):
        if lst[idx][1][1]>=maxh:
            maxi=idx
            maxh=lst[idx][1][1]

    if maxi==0:
        p=larea+(start[1]-maxh)*(stor[maxidx][1][0]-stor[maxi][1][0])
        return p
    
    else:
        p=larea+(start[1]-maxh)*(stor[maxidx][1][0]-stor[maxi][1][0])
        return leftarea(lst,maxi,start,p)

full=fullarea
if maxidx<stor[-1][0]:
    r=rightarea(stor,maxidx,start,0)
elif maxidx>=stor[-1][0]:
    r=0
if maxidx>stor[0][0]:
    l=leftarea(stor,maxidx,start,0)
elif maxidx<=stor[0][0]:
    l=0

print(full-r-l)