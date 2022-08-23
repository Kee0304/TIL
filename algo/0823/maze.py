from pprint import pprint

import sys
sys.stdin=open('sample_input(4).txt')

def maze(mat):
    global srow
    global scol
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1]
    visited=[]                                                                                                  # 방문지점을 저장할 리스트                
    stack=[]                                                                                                    # 지나온 길을 저장할 스택

    while 1:                                                                                                    # return 할 때까지 반복한다.

        for i in range(4):                                                                                      # 델타 탐색을 해서

            if mat[srow+drow[i]][scol+dcol[i]]==0 and ((srow+drow[i],scol+dcol[i]) not in visited):             # 0이고 방문하지 않은 지점이 있다면
                srow=srow+drow[i]                                                                               # 그 지점을 현재 지점으로 저장하고
                scol=scol+dcol[i]
                stack.append((srow,scol))                                                                       # 스택에 쌓고
                visited.append((srow,scol))                                                                     # 방문했음을 저장한다.
                break                                                                                           # stack[-2]에 대한 탐색을 중단한다.
                
            elif mat[srow+drow[i]][scol+dcol[i]]==3:                                                            # 3이면 도착했으므로 끝
                return 1
            
        else:                                                                                                   # 델타탐색을 했는데 0이고 방문한 적 없는 점을 못 찾았는데

            if stack:                                                                                           # 스택이 차 있으면
                stack.pop()                                                                                     # 스택에서 pop하고

                if stack:                                                                                       # 만약 그래도 스택이 차있으면 
                    srow=stack[-1][0]                                                                           # top의 지점을 현재 지점으로 바꾸고
                    scol=stack[-1][1]
                    continue                                                                                    # 루프를 계속
                    
                else:                                                                                           # 스택이 비어있으면
                    for row in range(N+2):                                                                      # 다시 시작지점을 찾아서 넣어줌         
                        for col in range(N+2):
                            if mat[row][col]==2:
                                srow,scol=row,col                     
                                continue

            else:                                                                                               # 스택이 비어 있으면
                return 0                                                                                        # 길이 없다는 뜻이다.                    

T=int(input())

for t in range(1,T+1):
    N=int(input())
    mat=[]
    mat.append([1]*(N+2))                               # 이탈을 막기 위해 벽으로 감싼다.
    for _ in range(N):
        mat.append([1]+list(map(int,input()))+[1])
    mat.append([1]*(N+2))

    for row in range(N+2):                              # 시작지점을 탐색한다.
        for col in range(N+2):
            if mat[row][col]==2:
                srow,scol=row,col                       # 시작지점이자, 현재 지점을 저장할 변수
                break
    
    print(f'#{t} {maze(mat)}')