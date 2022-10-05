



T = int(input())

for t in range(1,T+1):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]
    mincost=0
    for i in range(N):
        for j in range(N):
            if i == j:
                mincost+=mat[i][j]
