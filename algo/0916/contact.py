import sys
sys.stdin=open('input.txt')

def BFS(adj,s):                                            # BFS 탐색 함수. 연결 관계와 시작점을 받는다.
    q=[]                                                   # 큐
    visited=[]                                             # visited

    q.append(s)                                            # 큐에 시작점 추가
    visited.append(s)                                      # 방문 표시

    while 1:
        tmp=q[:]                                           # 일단 BFS 1회 전에 큐 상태를 저장
        for _ in range(len(q)):                            # 깊이가 같은 노드들을 한 번에 싹 돌아야 하므로 q의 길이에 대해 반복
            front=q.pop(0)                                 # front를 pop하고
            if front in adj:                               # 만약 front가 연결관계에 키로서 존재하면
                for next_node in adj[front]:               # front키에 해당하는 값(리스트형태, 갈 수 있는 다음 노드)에 대해
                    if next_node not in visited:           # 방문한 적이 없는 노드면
                        q.append(next_node)                # 큐에 추가하고
                        visited.append(next_node)          # 방문 표시
                
        if q==[]:                                          # BFS를 돌려서 큐가 비어있다는 뜻은 이전 큐의 모든 노드들에서 더 이상 갈 수 있는 지점이 없었다는 뜻이므로
            return tmp                                     # 이전 상태의 큐가 마지막에 동시에 연락받은 사람들이 된다.
            
for t in range(1,11):
    length, sp=map(int,input().split())                    # 데이터의 길이와 시작 노드
    datalist=list(map(int,input().split()))                # 일단 리스트 형태로 입력을 받고
    adjdict={}                                             # 연결 관계를 딕셔너리로 연결
    for idx in range(0,length-1,2):                        # from to from to이므로 from을 기준으로 하여 두 개를 간격으로 이동
        if adjdict.get(datalist[idx])==None:               # 만약 딕셔너리에 아직 키가 없으면
            adjdict[datalist[idx]]=[datalist[idx+1]]       # 키와 값 추가
        else:                                              # 딕셔너리에 이미 해당 키가 존재한다면
            adjdict[datalist[idx]].append(datalist[idx+1]) # 값 리스트에 값을 추가해준다.

    
    h=BFS(adjdict,sp)                                      # BFS 탐색
    print(f'#{t} {max(h)}')                                # 큐 중에서 가장 큰 놈을 출력