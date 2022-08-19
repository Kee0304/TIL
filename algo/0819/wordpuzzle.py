T=int(input())

for t in range(1,T+1):
    N,K=map(int,input().split())
    
    mat=[[] for _ in range(N)]                              # 들어오는 N*N의 0과 1들을 2차원 배열 형태로 저장하겠다.
    for i in range(N):
        mat[i] = list(map(int,input().split()))
                     
    rowlengthlist=[0]*(N+1)                                 # 1이 연속된 길이들을 저장할 리스트. append를 사용하지 못하므로 미리 만들어둔다.
    rowlen=[0]*(N+1)
    collengthlist=[0]*(N+1)
    collen=[0]*(N+1)

    # 먼저 행에 대해서 탐색
    for row in range(N):
        for col in range(N):
            if mat[row][col]==1: # 만약 mat[row][col]==1이면
                length=1         # 길이 1부터 시작
                for i in range(1,N-col):
                    if mat[row][col+i]==1:  # 현재 col에서 4까지 탐색한다.
                        length+=1
                    
                    else:
                        break   

                rowlengthlist[length]+=1    # 이 경우 길이가 4인 놈이 있을 경우 3에도 +1, 2에도 +1 등등이 되어있기 때문에 중복을 제거해줘야한다.
            
    for i in range(1,len(rowlengthlist)-1):
        rowlen[i]=rowlengthlist[i]-rowlengthlist[i+1]

    
    for col in range(N):
        for row in range(N):
            if mat[row][col]==1: # 만약 mat[row][col]==1이면
                length=1         # 길이 1부터 시작
                for i in range(1,N-row):
                    if mat[row+i][col]==1:  # 현재 row에서 4까지 탐색한다.
                        length+=1
                    
                    else:
                        break   

                collengthlist[length]+=1    # 이 경우 길이가 4인 놈이 있을 경우 3에도 +1, 2에도 +1 등등이 되어있기 때문에 중복을 제거해줘야한다.
            
    for i in range(1,len(collengthlist)-1):
        collen[i]=collengthlist[i]-collengthlist[i+1]
    

    word_cnt=0
    word_cnt+=rowlen[K]
    word_cnt+=collen[K]

    print(f'#{t} {word_cnt}')