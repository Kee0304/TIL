import sys
sys.stdin=open('sample_input(1).txt')

def bfs_isway(A,N):                                                                                                   # 길이 있는지 판별하는 함수
    drow=[-1,1,0,0]                                                                                                 # 상하좌우 델타탐색
    dcol=[0,0,-1,1]

    visited=[]                                                                                                      # 방문한 지점을 튜플로 저장할 리스트
    q=[]                                                                                                            # 활용할 queue
    
    for i in range(N+2):                                                                                             # 시작점 탐색
        for j in range(N+2):
            if A[i][j]==2:
                srow,scol=i,j
                break
    dist=0
    q.append((srow,scol))                                                                                           # 시작점 queue에 추가
    visited.append((srow,scol))                                                                                     # 시작점 방문표시                                                                                                     

    while 1:
        for _ in range(len(q)):
            q.pop(0)                                                                                                    # front를 pop한다.
            for delta in range(4):                                                                                      # 델타 탐색
                if A[srow+drow[delta]][scol+dcol[delta]]==0 and ((srow+drow[delta],scol+dcol[delta]) not in visited):   # 0이고 방문하지 않았으면    
                    q.append((srow+drow[delta],scol+dcol[delta]))                                                       # queue에 추가

                elif A[srow+drow[delta]][scol+dcol[delta]]==3:                                                          # 3이면
                    return dist                                                                                         # 도착했으므로 거리

            else:
                if q==[]:                                                                                               # 만약 queue가 비었으면
                    return 0                                                                                            # 탐색 실패
                else:                                                                                                   # queue가 아직 차있으면                                                                                                
                    visited.append(q[0])                                                                                # front를 방문표시하고
                    srow,scol = q[0]                                                                                    # front가 현재 지점이 된다.
                
        else:                                                                                                           # for 문이 끝까지 실행됐으면                                                                                                  # 아직 queue가 차 있으면
            dist+=1                                                                                                     # 거리 +1


T=int(input())    
for t in range(1,T+1):
    N=int(input())                                                                                                  # 지정된 형식대로 입력받고
    mat=[]
    mat.append([1]*(N+2))                                                                                               # 더미로 감싸주고
    for _ in range (N):
        mat.append([1]+list(map(int,list(input())))+[1])
    mat.append([1]*(N+2))

    print(f'#{t} {bfs_isway(mat,N)}')                                                                               # 지정된 형식대로 출력한다.