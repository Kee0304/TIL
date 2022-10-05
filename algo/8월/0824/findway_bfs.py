T= 10

def bfs(v, N, t):       # v 시작, N 마지막 정점, t 찾는 정점
    visited=[0]*(N+1)
    q=[]
    q.append(v)         # 시작점 큐에 추가
    visited[v]=1        # 시작점 방문 표시    
    while q:
        v=q.pop(0)      # dequeue
        if v==t:
            return 1

    return 0

for _ in range(T):
    tc,E=map(int,input().split())
    arr=list(map(int,input().split()))

    adjlist=[[] for _ in range(100)]
    for i in range(E):
        a,b=[i*2],arr[i*2+1]
        adjlist.append(b)
    
    bfs(0,99,99)