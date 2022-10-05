from pprint import pprint

def findway(start,end,adj,d):
    U=[start]
    for idx in range(len(adj)):           # 일단 시작점에 대해
        if adj[start][idx] == 1:          # 시작점의 인접점은
            d[idx]=1                      # 경로의 길이가 1이다.

    for _ in range(end-1):
        w=0
        for i in range(1, end+12):
            if (i not in U) and (d[i] < d[w]):
                w = i
        U.append(w)
        for v in range(1,end+12):
            if adj[w][v] == 1:
                d[v] = min(d[v], d[w] + adj[w][v])
    d[start]=0

    return d


T = int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    adj1 = [[1000000]*(2*(M+11)) for _ in range(2*(M+11))]
    for i in range(2*(M+11)):
        adj1[i][i] = 0
    if N<M:
        for n in range(1,M+11):
            adj1[n][n-1]=1
            adj1[n][n+1]=1
            adj1[n][2*n]=1
            if n>=10:
                adj1[n][n-10]=1

    dout = [1000000]*(2*(M+11))
    result=findway(N,M,adj1,dout)

    print(f'#{t} {result[M]}')