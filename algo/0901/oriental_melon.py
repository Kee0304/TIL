K=int(input())


arr=[]
for _ in range(1,6+1):
    a=list(map(int,input().split()))
    arr.append(a)

arr3=arr*3

maxgaro=0
maxsero=0
for i in range(6,12):
    if arr3[i][0]==3 or arr3[i][0]==4:
        if arr3[i][1]>maxsero:
            maxsero=arr3[i][1]
            maxseroidx=i
    
    else:
        if arr3[i][1]>maxgaro:
            maxgaro=arr3[i][1]
            maxgaroidx=i

if arr3[maxgaroidx-1][1]-arr3[maxgaroidx+1][1]>0:
    partsero=arr3[maxgaroidx-1][1]-arr3[maxgaroidx+1][1]
else:
    partsero=(-1)*(arr3[maxgaroidx-1][1]-arr3[maxgaroidx+1][1])

if arr3[maxseroidx-1][1]-arr3[maxseroidx+1][1]>0:
    partgaro=arr3[maxseroidx-1][1]-arr3[maxseroidx+1][1]
else:
    partgaro=(-1)*(arr3[maxseroidx-1][1]-arr3[maxseroidx+1][1])

fullsize=maxgaro*maxsero
restpart=partgaro*partsero
area=fullsize-restpart
print(area*K)





