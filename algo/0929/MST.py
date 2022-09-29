T= int(input())

def prim(node):
    mst= [0]*(V+1)              # 노드들이 mst에 들어가 있는지 판별
    key=[float('inf')]*(V+1)    # 지금 상태에서 해당 인덱스까지 가는 데에 얼마만큼의 weight가 있는지
    parent= [-1]*(V+1)
    key[node]=0                 # 임의의 시작지점에 대해 key를 0으로 잡음(자기 자신)

    for _ in range(V+1):        # 노드 수 만큼 반복
        min_val = float('inf')  # 최소 값을 무한대로 초기화

        for i in range(V+1):    # 노드들에 대해
            if mst[i] == 0 and key[i] < min_val:    # 만약 노드가 mst에 없고 값이 최소값보다 작다면
                s = i                               # 노드 번호를 저장하고
                min_val = key[i]                    # 최소값 역시 저장
        
        mst[s] = 1                                  # for 문을 다 돌아서 나온 노드를 mst에 넣어줌

        for e in range(V+1):                         
            if mst[e] == 0 and adj[s][e] > 0 :      # 방문한 적이 없고 방금 나온 s와 인접한 점 e에 대해
                if key[e] > adj[s][e]:              # 그 값이 현재 key값보다 작으면
                    key[e] = adj[s][e]              # key값 교체
                    parent[e]=s                     # 부모를 s로 바꿔줌

    return sum(key)
            

for t in range(1,T+1):
    V,E = map(int,input().split())
    wgraph=[]
    adj=[[0]*(V+1) for _ in range (V+1)]
    for _ in range(E):
        n1,n2,w = map(int,input().split())
        wgraph.append([n1,n2,w])
        adj[n1][n2] = w
        adj[n2][n1] = w
    

    result=prim(0)
    print(f'#{t} {result}')