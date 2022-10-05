import sys
from collections import deque

sys.stdin = open('input.txt')

def tyk():              # 붕어빵 함수
    second=0            # 현재 시간
    taisecond=0         # 붕어빵 타이머
    tai=0               # 붕어빵 개수
    while 1:
        if taisecond==M:# 만약 붕어빵 타이머가 M과 같으면
            tai+=K      # 붕어빵 K개 추가
            taisecond=0 # 타이머 초기화

        while len(customer)>=1 and second==customer[0]: # 고객이 존재하고 현재 초=고객방문 시간 이면 계속 반복
            customer.popleft()  # 맨 앞 고객에게
            tai-=1              # 붕어빵을 주고 보낸다.
            if tai < 0:         # 만약 붕어빵 개수가 음수가 되면
                return 'Impossible' # 실패
        
        if len(customer)==0:    # 만약 while 문이 끊기지 않고 다 돈 뒤 남은 손님이 없으면
            return 'Possible'   # 성공
        
        # 붕어빵도 올 손님도 남아있으면
        taisecond+=1            # 타이머 +1
        second+=1               # 현재 시간 +1

        

T = int(input())

for t in range(1,T+1):
    N,M,K = map(int,input().split())
    inlist=sorted(list(map(int,input().split())))   # 손님 도착 시간은 무작위로 주어져있으므로 오름차순 정렬한다.
    customer=deque(inlist)                          # deque 사용
    result=tyk()

    print(f'#{t} {result}')