from collections import deque

def bfs(start,end,dq):
    cnt=0
    dq.append(start)
    visited=set()
    while 1:
        for _ in range(len(dq)):
            front=dq.popleft()
            visited.add(front)
            ad=[front-10,front-1,front+1,front*2]
            for num in ad:
                if num<=1000000 and 1<=num:
                    if num not in visited:
                        if num == end:
                            cnt+=1
                            return cnt
                        else:
                            dq.append(num)
                            visited.add(num)
        print(dq)
        cnt+=1

T = int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())

    q=deque()
    result=bfs(N,M,q)

    print(f'#{t} {result}')