from pprint import pprint
import sys
sys.stdin = open('sample_input.txt')

#def greedy(mat):
#    current=[0,0]
#    sum=mat[current[0]][current[1]]
#    while 1:
#        print(mat[current[0]][current[1]])
#        if current[0]+1<=len(mat)-1 and current[1]+1<=len(mat)-1:
#            if mat[current[0]+1][current[1]]>mat[current[0]][current[1]+1]:
#                current=[current[0],current[1]+1]
#                sum+=mat[current[0]][current[1]]
#            elif mat[current[0]+1][current[1]]<=mat[current[0]][current[1]+1]:
#                current=[current[0]+1,current[1]]
#                sum+=mat[current[0]][current[1]]
#        elif current[0]+1<=len(mat)-1 and current[1] == len(mat)-1:
#            current=[current[0]+1,current[1]]
#            sum+=mat[current[0]][current[1]]
#        elif current[0] == len(mat)-1 and current[1]+1<=len(mat)-1:
#            current=[current[0],current[1]+1]
#            sum+=mat[current[0]][current[1]]
#        else:
#            return sum
# 그리드하게 해뵜는데 안 되네....

#def minsum(mat,N):
#    mat[0][0][1]=mat[0][0][0]                             # 0,0인 놈은 누적이 자기 자신
#    for i in range(N):
#        for j in range(N):
#            if i == 0 and j == 0 :                        # 처음인 놈은 이미 조작했음
#                pass
#            elif i == 0 and j != 0:
#                mat[i][j][1]=mat[i][j][0]+mat[i][j-1][1]  # 0행에 있는 놈들은 왼쪽에서만 옴
#            
#            elif i != 0 and j == 0:
#                mat[i][j][1]=mat[i][j][0]+mat[i-1][j][1]  # 0열에 있는 놈들은 위쪽에서만 옴
#        
#    for i in range(1,N):
#        for j in range(1,N):
#            if mat[i-1][j][1]>mat[i][j-1][1]:             # 위와 왼쪽 누적을 비교해서 위가 크면
#                mat[i][j][1]=mat[i][j][0]+mat[i][j-1][1]  # 왼쪽 놈을 선택
#            else:                                         # 왼쪽 누적이 크면
#                mat[i][j][1]=mat[i][j][0]+mat[i-1][j][1]  # 위쪽에서 온 걸로 한다.
#
#    return mat
#            
#                
#
#T=int(input())
#
#for t in range(1, T+1):
#    N=int(input())
#    mat=[list(map(int,input().split())) for _ in range(N)]  # 2차원 행렬로 받아서
#    for i in range(N):
#        for j in range(N):
#            mat[i][j]=[mat[i][j],0]                         # 3차원 행렬로 변환
#                                                            # [원래수,누적] 형태로 사용
#    
#    print(f'#{t} {minsum(mat,N)[N-1][N-1][1]}')
    
def minsum(mat,N):
    acmat=[[0]*N for _ in range(N)]                  # 누적을 저장할 2차원 배열
    acmat[0][0]=mat[0][0]                            # 0,0인 놈은 누적이 자기 자신

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0 :                   # 처음인 놈은 이미 조작했음
                pass
            elif i == 0 and j != 0:
                acmat[i][j]=mat[i][j]+acmat[i][j-1]  # 0행에 있는 놈들은 왼쪽에서만 옴
            
            elif i != 0 and j == 0:
                acmat[i][j]=mat[i][j]+acmat[i-1][j]  # 0열에 있는 놈들은 위쪽에서만 옴

    for i in range(1,N):
        for j in range(1,N):
            if acmat[i-1][j]>acmat[i][j-1]:          # 위와 왼쪽 누적을 비교해서 위가 크면
                acmat[i][j]=mat[i][j]+acmat[i][j-1]  # 누적=현재+왼쪽 놈의 누적 

            else:                                    # 왼쪽 누적이 크면
                acmat[i][j]=mat[i][j]+acmat[i-1][j]  # 누적=현재+위 쪽 놈의 누적

    return acmat
            
T=int(input())

for t in range(1, T+1):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]  # 2차원 행렬로 받아서
    
    print(f'#{t} {minsum(mat,N)[N-1][N-1]}')