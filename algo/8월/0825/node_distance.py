import sys
sys.stdin=open('sample_input(3).txt')

def bfs_minway(A,S,G):                                       # A 연결관계 딕셔너리 S 시작지점 G 골

    visited=[]                                               # 방문한 지점을 튜플로 저장할 리스트
    q=[]                                                     # 활용할 queue

    dist=0
    q.append(S)
    visited.append(S)
                                                                                                           
    while 1:
        for _ in range(len(q)):                              # 같은 깊이(?)의 노드에 대해서 전부 실행한다.
            q.pop(0)                                         # front를 dequeue하고

            for node in A[S]:                                # key(현재지점)에 인접한 노드에 대해서
                if node==G:                                  # 골이면
                    dist+=1                                  # 길이를 +1 하고
                    return dist                              # 길이를 반환

                elif node!=G and (node not in visited):      # 골이 아닌 노드고 아직 방문한 적이 없으면
                    q.append(node)                           # queue에 node들을 추가한다.

            else:                                            # for문이 다 돌았으면=골이 없었으면
                if q==[]:                                    # 만약 queue가 비었으면
                    return 0                                 # 탐색 실패                                            
                else:
                    visited.append(q[0])                     # front를 방문표시하고
                    S=q[0]                                   # queue의 front를 현재지점으로 갱신

        else:                                                # 아직 queue가 차 있으면
            dist+=1                                          # 길이를 +1 한다.


T=int(input())
for t in range(1,T+1):
    V,E=map(int,input().split())

    adjdict={}
    for _ in range(E):
        adj=list(map(int,input().split()))
        if len(adj)==2:
            try:                                                 # 만약 딕셔너리에 a라는 키가 존재하면
                adjdict[adj[0]].append(adj[1])                             # 그 value에 b를 append 해준다.
            except:                                              # 만약 a라는 키가 없어서 오류가 나면
                adjdict[adj[0]]=[adj[1]]                                   # 새로운 키와 값(리스트)를 넣어준다.
            try:
                adjdict[adj[1]].append(adj[0])
            except:
                adjdict[adj[1]]=[adj[0]]

        else:
            adjdict[adj[0]]=[]

    S,G=map(int,input().split())

    print(f'#{t} {bfs_minway(adjdict,S,G)}')