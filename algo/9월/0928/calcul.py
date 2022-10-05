from pprint import pprint

def findway(start,end,adj,d):
    for idx in range(len(adj)):
        if adj[start][idx] == 1:
            d[idx]=1
    
    cidx=start+1
    while cidx<2*(end+11):
        for v in range(1,2*(end+11)):     # 정점 v가
            if adj[cidx][v]==1:           # cidx에 인접이면
                d[v] = min(d[v], d[cidx] + adj[cidx][v])
        cidx+=1

    return d

    

T = int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    adj1 = [[1000000]*(2*(M+11)) for _ in range(2*(M+11))]
    for i in range(2*(M+11)):
        adj1[i][i] = 0
    if N<M:
        for n in range(N,M+11):
            adj1[n][n-1]=1
            adj1[n][n+1]=1
            adj1[n][2*n]=1
            if n>=10:
                adj1[n][n-10]=1

    dout = [1000000]*(2*(M+11))
    result=findway(N,M,adj1,dout)

    print(f'#{t} {result[M]}')