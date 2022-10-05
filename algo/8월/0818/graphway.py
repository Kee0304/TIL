import sys
sys.stdin=open('sample_input(2).txt')

T=int(input())

for t in range(1,T+1):
    V,E=map(int,input().split())

    adjlist=[]
    node=[]

    for _ in range(E):
            num1,num2=map(int,input().split())  
            node.append(num1)
            node.append(num2)
            adjlist.append([num1,num2])

    S,G=map(int,input().split())


    nodeac=len(set(node))                    # set을 통해 노드의 개수를 구함
    nodelist=list(set(node))


    adjdict={}                                  

    for lst in nodelist:
        adjdict[lst]=[]

    for li in adjlist:
        adjdict[li[0]].append(li[1])

    for key, value in adjdict.items():
        if value ==[]:
            value.append(None)
          

    visited=[0]*E
    stack=[0]*E

    def findway(s,g):
        top=-1                      # 시작한다.
        visited[s]=1                # 시작점은 이미 방문한 상태


        while 1:
            for w in adjdict[s]:    # v에서 갈 수 있는 노드 w 중에
                if w == g :         # w가 도착점이면
                    return 1        # 1을 반환

                elif (w!=None) and (visited[w]==0) :   # 방문한 적 없는 노드이면
                    top += 1           # 방문하고
                    stack[top]=s       # 스택에 v를 넣어준 다음
                    s=w                # 현재 위치를 w로 갱신한 다음
                    visited[w]=1       # 방문 여부를 표시
                    break
                
                elif (w==None):     # 더 이상 방문할 수 있는 노드가 없는데
                    if top != -1:       # 스택이 비어있지 않다면
                        s=stack[top]
                        top -= 1        # 이전 노드로 돌아간다.


                    else:           # 스택이 비어있다 = 가능한 모든 방문을 했는데 w==99가 없었다면
                        return 0    # 방문 실패

                elif (visited[w]==1) and (w!=adjdict[s][-1]) :    # w를 이미 방문했는데 w가 adjlist[v]의 마지막이 아니면 
                    continue

                elif (visited[w]==1) and (w==adjdict[s][-1]) :    # w를 이미 방문했는데 w가 adjlist[v]의 마지막이라면
                    if top != -1:       # 스택이 비어있지 않다면
                        s=stack[top]
                        top -= 1        # 이전 노드로 돌아간다.


                    else:           # 스택이 비어있다 = 가능한 모든 방문을 했는데 w==99가 없었다면
                        return 0    # 방문 실패

            
    print(f'#{t} {findway(S,G)}')