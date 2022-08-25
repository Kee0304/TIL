import sys
sys.stdin=open('sample_input(3).txt')

T=int(input())

def permutsum(N, res, subsum, row):   # N: 배열 크기 res: idx를 담을 배열, subsum:현재까지 누적합, row: 현재 열
    
    if row==N:
        if minsum>subsum:
            minsum=subsum
        return

    for i in range(N):
        if i not in res:
            if subsum + mat[row][i] >= minsum:
                continue
            res.append(i)
            permutsum(N,res,subsum+mat[row][i],row+1)
            res.pop()



for t in range(1,T+1):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]

    res=[]
    minsum=N**3
    permutsum(N,res,0,0)

    print(f'#{t} {minsum}')

    

    




