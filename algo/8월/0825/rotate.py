import sys
sys.stdin=open('sample_input.txt')

T=int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    numlist=list(map(int,input().split()))

    for _ in range(M):                      
        a=numlist.pop(0)                    # 앞에 거 빼서
        numlist.append(a)                   # 뒤에 집어넣는다.
        

    print(f'#{t} {numlist[0]}')