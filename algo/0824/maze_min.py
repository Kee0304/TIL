def dfs(i,j,s,N):
    global minV
    if maze[i][j] ==3:
        if minV > s:
            minV = s
        return

    else:
        visited[i][j]=1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj=i+di,j+dj
            if maze[ni][nj]!=1 and visited[ni][nj]==0:
                dfs(ni,nj,s+1,N)
        visited[i][j]=0
        return

T = int(input())
for r in range(1, T+1):
    N= int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti = -1
    stj = -1


    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti,stj=i,j
                break
        if sti!=1:
            break
