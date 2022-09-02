mat=[]
numlist=[]
for _ in range(5):
    mat.append(list(map(int,input().split())))
for _ in range(5):
    numlist+=list(map(int,input().split()))

print(bingocnt(mat,numlist))

