T=int(input())

for t in range(1,T+1):
    N=int(input())
    mat=[[0 for _ in range(N)] for _ in range(N)]               # 0으로 채워진 2차원 배열을 만들거다.
    
    num=1

    if N%2==0:                                                  # 짝수면
        for i in range(N//2):                                   # N을 2로 나눈 몫만큼의 range 범위에서
            for col in range(0+i,N-i):                          # 오른쪽으로 쭈욱
                mat[0+i][col]=num
                num+=1

            for row in range(1+i,N-i):                          # 아래로 쭈욱
                mat[row][N-1-i]=num
                num+=1

            for col in range(N-2-i,-1+i,-1):                    # 왼쪽으로 쭈욱
                mat[N-1-i][col]=num
                num+=1

            for row in range(N-2-i,0+i,-1):                     # 위로 쭈욱 숫자에 부딪히기 전까지 1씩 커지면서 숫자를 채워넣는다.
                mat[row][0+i]=num
                num+=1


    else:
        for i in range(N//2):                                   # 홀수면 나머지는 다 똑같은데
            for col in range(0+i,N-i):
                mat[0+i][col]=num
                num+=1

            for row in range(1+i,N-i):
                mat[row][N-1-i]=num
                num+=1

            for col in range(N-2-i,-1+i,-1):
                mat[N-1-i][col]=num
                num+=1

            for row in range(N-2-i,0+i,-1):
                mat[row][0+i]=num
                num+=1

            pprint(mat)

        mat[N//2][N//2]=num                                     # 마지막 남는 정 가운데를 채워준다.


    print(f'#{t}')
    for row in mat:
        print(" ".join(map(str,row)))                           # 각 행의 요소들을 map을 통해 문자열로 바꿔주고, join을 통해 띄어쓰기를 기준으로 하여 문자열로 변환한 뒤, 출력한다.
