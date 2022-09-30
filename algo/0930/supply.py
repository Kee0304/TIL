import sys
from collections import deque

sys.stdin=open('input.txt')

def dijkstra():
    delta_search=[[-1,0],[1,0],[0,-1],[0,1]]

    while dq:                                                                                   # 덱이 차있는 동안 반복
        for _ in range(len(dq)):                                                                # 덱의 길이 만큼 반복(BFS)
            row, col, acctime = dq.popleft()                                                    # front를 pop해서 행, 열, 누적 시간 저장

            #if dismat[row][col] < acctime:                                                      # 만약 여태까지 갱신된 누적시간이 지금 누적 시간 보다 작으면
            #    continue                                                                        # 현재 for반복을 중단시키고 다음 for 반복으로 넘어간다.

            if dismat[row][col] >= acctime:                                                                               # 지금 뽑은 누적 시간이 더 짧으면
                for delta in delta_search:                                                      # 델타 탐색 실행
                    adj_row = row + delta[0]                                                    
                    adj_col = col + delta[1]
                    if 0<=adj_row<N and 0<=adj_col<N:                                           # 범위 내의 행과 열에 대해서
                        if acctime + roadmat[adj_row][adj_col] < dismat[adj_row][adj_col]:      # 만약 지금까지 누적 시간 + 델타 탐색에 있는 지점의 복구 시간이 델타 탐색에 있는 지점의 누적 복구 시간 보다 짧으면
                            dismat[adj_row][adj_col] = acctime + roadmat[adj_row][adj_col]      # 해당 지점의 누적 복구 시간을 갱신해준다.
                            dq.append((adj_row,adj_col,acctime + roadmat[adj_row][adj_col]))    # 덱에 해당 지점을 추가해준다.



T = int(input())

for t in range(1,T+1):
    N = int(input())
    roadmat=[list(map(int,list(input().rstrip()))) for _ in range(N)]
    dismat=[[1000000]*N for _ in range(N)]
    dismat[0][0]=0
    start=(0,0,roadmat[0][0])
    dq=deque()
    dq.append(start)
    dijkstra()
    print(f'#{t} {dismat[N-1][N-1]}')