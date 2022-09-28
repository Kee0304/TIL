import sys
sys.stdin = open('sample_input(3).txt', 'r')

T = int(input())

for t in range(1,T+1):
    N=int(input())
    inlist=[None]*N                               # 인풋들을 저장할 리스트
    sch=[]                                        # 조건에 맞는 놈들을 저장할 리스트
    for n in range(N):
        s,e=map(int,input().split())
        inlist[n]=(s,e)                           # 튜플 형식으로 저장
    inlist = sorted(inlist, key=lambda x:x[1])    # 종료시간을 기준으로 정렬

    sch.append(inlist[0])                         # 일단 종료시간이 가장 빠른 놈을 저장
    for idx in range(1,len(inlist)):
        if inlist[idx][0]>=sch[-1][1]:            # 만약 이전 sch에 들어있는 마지막 놈의 종료시간보다
            sch.append(inlist[idx])               # 현재 놈의 시작 시간이 뒤라면 추가
            
    print(f'#{t} {len(sch)}')