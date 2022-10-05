import sys
sys.stdin=open('input.txt')

T=int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())

    mat=[[] for _ in range(N)]                              # 들어오는 N*N의 수들을 2차원 배열 형태로 저장하겠다.
    for i in range(N):
        mat[i] = list(map(int,input().split()))
    
    maxkill=0                                               # 최대 사살 수를 저장할 변수
    for row in range(N-M+1):                                # 행, 렬 모두 인덱스를 N-M까지 돌면 되니 range(N-M+1)로 잡아준다. 
        for col in range(N-M+1):
            kill=0                                          # 한 번의 동작에서 죽이는 파리 수
            for i in range(M):                              # M*M 크기의 사각형 내에 있는 파리 수=죽인 수
                for j in range(M):                          
                    kill+=mat[row+i][col+j]                 # 행 고정 -> 열에 있는 애들 더하기 -> 행 이동
            if kill>maxkill:                                # 만약 나온 킬 수가 현재 maxkill보다 크면
                maxkill=kill                                # 나온 킬 수를 maxkill로 바꿔준다.
    
    print(f'#{t} {maxkill}')