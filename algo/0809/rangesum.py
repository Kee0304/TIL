T=int(input())

for test_case in range(1, T+1):
    N, M=((input().rstrip()).split())
    N=int(N)
    M=int(M)
    numlist=list(map(int,(input().rstrip()).split()))

    maxsum=0
    minsum=0

    for i in range(0,M):
        maxsum+=numlist[-1-i]
        minsum+=numlist[0+i]
    
    for idx in range(0,N-M+1):
        ransum=0
        for ran in range(0,M):
            ransum+=numlist[idx+ran]
        
        if ransum>maxsum:
            maxsum=ransum
        elif ransum<minsum:
            minsum=ransum


    print(f'#{test_case} {maxsum-minsum}')
