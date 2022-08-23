import sys
sys.stdin=open('sample_input(3).txt')

T=int(input())




for t in range(1,T+1):
    N=int(input())
    mat=[list(map(int,input().split())) for _ in range(N)]

    sumlist=[]
    rmat=list(zip(*mat))                                                                # 전치행렬을 생성해서 계산을 편하게 할 거다

    lst=[]
    def permut(idx, n, r, res):
        if idx==r: 
            lst.append(res[:])  # 슬라이싱이 없다면 얕은 복사와 같은 현상이 일어난다.
            return
        for i in range(n):
            if i not in res: # if 분기가 없다면 중복
                res.append(i)
                permut(idx + 1,n, r, res)
                res.pop()

    permut(0,N,N,[])

    minsum=N**3
    
    for subpermu in lst:                                                                # 길이가 N인 순열들에 대해
        subsum=0                                                                        
        for i in range(N):
            subsum+=rmat[i][subpermu[i]]                                                 # 인덱스에 대해 
            if subsum>minsum:
                break

        if subsum<minsum:
            minsum=subsum
    
    print(f'#{t} {minsum}')

    

    




