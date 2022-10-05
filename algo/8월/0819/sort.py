import sys
sys.stdin=open('input.txt')

T = int(input())


for t in range(1,T+1):
    N=int(input())
    numlist=list(map(int,input().split()))

    for idx in range(N-1,-1,-1):                                        # 버블 소트
        for j in range(0,idx):
            if numlist[j]>numlist[j+1]:
                numlist[j],numlist[j+1] = numlist[j+1],numlist[j]

    numstr=" ".join(map(str,numlist))

    print(f'#{t} {numstr}')