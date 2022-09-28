T = int(input())

for t in range(1,T+1):
    N=int(input())
    farmmat=[list(map(int,list(input()))) for _ in range(N)]    # 받아서 리스트로 만들고 정수로 map
    farm=0
    for row in range(N//2):                                     # 0에서 N//2-1 행까지는
        for col in range(N//2-row,N//2+row+1):                  # 행에 따라 점점 길어짐
            farm += farmmat[row][col]                           # 다 더해줌
    for col in range(N):                                        # 크기는 항상 홀수니까 중앙이 남는다.
        farm += farmmat[N//2][col]                              # 다 더해
    for row in range(N//2+1,N):                                 # N//2+1에서 N-1행 까지는
        for col in range(N//2-(N-row)+1,N//2+(N-row)):          # 행에 따라 점점 짧아짐
            farm += farmmat[row][col]                           # 다 더해줌

    print(f'#{t} {farm}')