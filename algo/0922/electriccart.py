import sys

sys.stdin=open('sample_input(1).txt')

def f(i, r):                   # 현재 인덱스 i와 원하는 순열의 길이 r에 대해
    global able_arr
    if i==r:                   # 만약 현재 인덱스가 순열의 길이와 같다=bit의 길이가 원하는 순열의 길이와 같아지면
        an=bit[:r][:]          # 출력
        able_arr.append([1]+an+[1])
        return
    for n in range(2,N+1):
        if n not in bit[0:i]:  # 이전까지를 탐색해서 n이 들어있지 않다면(=중복검사)
            bit[i] = n         # n을 넣는다.
            f(i+1,r)           # 다음 인덱스를 채워넣으러 간다.
            bit[i] = None

T=int(input())

for t in range(1,T+1):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]
    able_arr=[]
    bit=[0]*(N-1)
    f(0,N-1)
    
    minelec=100*N                               # 최소 전력 소비량이 저장될 변수
    for i in range(len(able_arr)):                 # 가능한 방문 순서들에 대해
        elec=0                                  # 이번 순서에 대한 전력 소비량 초기화
        for j in range(N):                      # 방문 순서 길이에 대해
            elec+=mat[able_arr[i][j]-1][able_arr[i][j+1]-1]  # 방문 순서 인덱스에 대해 전력을 더해간다.
        if elec<minelec:                        # 만약 이 방문 순서의 전력 소비량이 이전 최소값 보다 작으면
            minelec=elec                        # 저장
        
    print(f'#{t} {minelec}')