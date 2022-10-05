import sys
sys.stdin=open('input.txt')

def bfs_isway(A):                                                                                                   # 길이 있는지 판별하는 함수
    drow=[-1,1,0,0]                                                                                                 # 상하좌우 델타탐색
    dcol=[0,0,-1,1]

    visited=[]                                                                                                      # 방문한 지점을 튜플로 저장할 리스트
    q=[]                                                                                                            # 활용할 queue
    
    for i in range(16):                                                                                             # 시작점 탐색
        for j in range(16):
            if A[i][j]==2:
                srow,scol=i,j
                break
    
    q.append((srow,scol))                                                                                           # 시작점 queue에 추가
    visited.append((srow,scol))                                                                                     # 시작점 방문표시
                                                                                                           

    while 1:
        q.pop(0)                                                                                                    # front를 pop한다.
        for delta in range(4):                                                                                      # 델타 탐색
            if A[srow+drow[delta]][scol+dcol[delta]]==0 and ((srow+drow[delta],scol+dcol[delta]) not in visited):   # 0이고 방문하지 않았으면    
                q.append((srow+drow[delta],scol+dcol[delta]))                                                       # queue에 추가
                
            elif A[srow+drow[delta]][scol+dcol[delta]]==3:                                                          # 3이면
                return 1                                                                                            # 도착했으므로 1 반환
            
        else:                                                                                                       # for 문이 끝까지 실행됐는데
            if q==[]:                                                                                               # 만약 queue가 비었으면
                return 0                                                                                            # 탐색 실패

            else:                                                                                                   # 아직 queue가 차 있으면
                visited.append(q[0])                                                                                # front를 방문표시하고
                srow,scol = q[0]                                                                                    # front가 현재 지점이 된다.


    
for _ in range(1,11):
    T=int(input())                                                                                                  # 지정된 형식대로 입력받고
    mat=[]
    for _ in range (16):
        mat.append(list(map(int,list(input()))))

    print(f'#{T} {bfs_isway(mat)}')                                                                                 # 지정된 형식대로 출력한다.