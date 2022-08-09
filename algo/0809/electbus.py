T=int(input())

for test_case in range(1, T+1):
    K,N,M=input().split()
    K=int(K)                                             # 한 번 충전으로 갈 수 있는 최대 정류장
    N=int(N)                                             # 종점
    M=int(M)                                             # 충전기가 있는 정류장 수

    m_list=list(map(int,input().split()))                # 충전기가 있는 정류장 번호를 인풋으로 받아 정수 리스트로 변환

    m_exist=[0]*(N+1)                                    # 충전기가 있는 정류장에 1을 표시할 리스트를 만들 거다.
    
    for sta in m_list:
        m_exist[sta]=1

    # 0에서 시작해서 K보다 작은 인덱스를 가진 충전기가 있는 정류장 중 가장 큰 놈에만 들르면 된다.

    station_list=[0]                                      # 정차할 정류장 리스트

    for i in station_list:                            
        if i+K<N:                                         # K 움직여서 아직 종점에 도착할 수 없으면
            for move in range(K,0,-1):                    # 가장 멀리부터 탐색한다.
                if m_exist[i+move]==1:                    # 갈 수 있는 범위 내에 정류장이 있으면
                    station_list.append(i+move)           # 갈 수 있는 가장 먼 정류장을 추가하고                          
                    break                                 # 다시 탐색을 시작한다.

    if N-station_list[-1]>K:                              # 종점과 station_list의 제일 끝 놈의 차가 K보다 크면
        print(f'#{test_case} 0')                          # 실패 
    else:
        print(f'#{test_case} {len(station_list[1:])}')    # 가장 앞에 0을 뺀 리스트의 길이가 충전횟수