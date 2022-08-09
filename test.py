T=int(input())

for test_case in range(1, T+1):
    K,N,M=input().split()
    K=int(K)                                             # 한 번 충전으로 갈 수 있는 최대 정류장
    N=int(N)                                             # 종점
    M=int(M)                                             # 충전기가 있는 정류장 수

    charger=list(map(int,input().split()))                # 충전기가 있는 정류장 번호를 인풋으로 받아 정수 리스트로 변환

    busstop=[0]*(N+1)
    for cha in charger:
        busstop[cha]+=1

    print(busstop)

    cnt=0
    bus=0

    
    while bus + K <N:
        for move in range(K,0,-1):
            if busstop[bus+move]==1:
                bus = bus+move
                cnt +=1
        
    else:
        cnt=0
        



    print(cnt)
