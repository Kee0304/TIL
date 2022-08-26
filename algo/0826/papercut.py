import sys
sys.stdin=open('paper_input.txt')

maxX,maxY=map(int,input().split())
cutnum=int(input())
vertex=[[0,maxY],[0,maxX]]
for _ in range(cutnum):
    A,B=map(int,input().split())
    vertex[A].append(B)

for i in range(2):
    vertex[i]=sorted(vertex[i])

vertex[0],vertex[1]=vertex[1],vertex[0]


maxarea=0
for x in range(1,len(vertex[0])):
    for y in range(1,len(vertex[1])):
        partarea=(vertex[0][x]-vertex[0][x-1])*(vertex[1][y]-vertex[1][y-1])
        if partarea>maxarea:
            maxarea=partarea

print(maxarea)
    
    


