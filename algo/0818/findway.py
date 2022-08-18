import sys
sys.stdin=open('input.txt')

for _ in range(1,11):

    T,N=map(int,input().split())
    waylist=list(map(int,input().split()))                        # 한 줄로 입력되는 길들을 일단 리스트로 저장
                  
    nodeac=len(set(waylist))                                      # set을 통해 노드의 개수를 구함
    nodelist=list(set(waylist))               
    waymat = [[] for _ in range(N)]                               # 길들을 나누어 저장할 변수
                  
    for i in range(N):                
        waymat[i].append(waylist[2*i])                            # 리스트에서
        waymat[i].append(waylist[2*i+1])                          # 2개씩 끊어서 넣어준다.
                  
                      
    adjdict={}                                                    # 원래는 리스트로 했는데 씹새들이 노드를 하나 건너 뛰어놨다.

    for lst in nodelist:
        adjdict[lst]=[]

    for li in waymat:
        adjdict[li[0]].append(li[1])

    for key, value in adjdict.items():
        if value ==[]:
            value.append(None)
          

    visited=[0]*N
    stack=[0]*N

    def findway(v):
        top=-1                                                    # 시작한다.
        visited[v]=1                                              # 시작점은 이미 방문한 상태


        while 1:
            for w in adjdict[v]:                                  # v에서 갈 수 있는 노드 w 중에
                if w == 99 :                                      # w가 도착점이면
                    return 1                                      # 1을 반환

                elif (w!=None) and (visited[w]==0) :              # 방문한 적 없는 노드이면
                    top += 1                                      # 방문하고
                    stack[top]=v                                  # 스택에 v를 넣어준 다음
                    v=w                                           # 현재 위치를 w로 갱신한 다음
                    visited[w]=1                                  # 방문 여부를 표시
                    break
                
                elif (w==None):                                   # 더 이상 방문할 수 있는 노드가 없는데
                    if top != -1:                                 # 스택이 비어있지 않다면
                        v=stack[top]
                        top -= 1                                  # 이전 노드로 돌아간다.

                    else:                                         # 스택이 비어있다 = 가능한 모든 방문을 했는데 w==99가 없었다면
                        return 0                                  # 방문 실패

                elif (visited[w]==1) and (w!=adjdict[v][-1]) :    # w를 이미 방문했는데 w가 adjlist[v]의 마지막이 아니면 
                    continue

                elif (visited[w]==1) and (w==adjdict[v][-1]) :    # w를 이미 방문했는데 w가 adjlist[v]의 마지막이라면
                    if top != -1:                                 # 스택이 비어있지 않다면
                        v=stack[top]
                        top -= 1                                  # 이전 노드로 돌아간다.


                    else:                                         # 스택이 비어있다 = 가능한 모든 방문을 했는데 w==99가 없었다면
                        return 0                                  # 방문 실패

            
    print(f'#{T} {findway(0)}')

