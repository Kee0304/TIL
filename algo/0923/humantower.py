def func(idx, n, r, res, minminus):      # n:원소의 범위
    if idx == r:               # 현재 인덱스가 원하는 조합의 길이 r과 같을 때
        tmp=res[:]
        comb.append(tmp) 
        return 
 
    start = idx                  # 아직 길이에 도달하지 않았으면 start=0으로 하고
    if res:                    # res가 존재할 때
        start = max(res)   # 지금 res 안에 있는 놈들 보다 큰 놈들만 넣으면 된다.                     
        # start = max(res)     # +1이 없다면 중복 허용
 
    for i in range(start, n):  # start에서 n-1까지
        res.append(list[i])          # res에 i를 더해주고
        func(idx+1, n, r, res, list) # 인덱스를 하나 올려 함수 실행
        res.pop()              # res의 마지막 놈을 빼준다. i에 대한 루프가 끝나고 이 후엔 i+1에 대해 루프가 시작할 것이다.

        # func(idx+1, n, r , res + [i])
        



T=int(input())

for t in range(1,T+1):
    N,B = map(int,input().split())
    heightlist=list(map(int,input().split()))
    comb=[]
    #for r in range(1,N+1):
    func(0,N,4,[],heightlist)
    
    minminus=100
    print(comb)
    for part in comb:
        if minminus>sum(part)-B and sum(part)-B>=0 :
            minminus=sum(part)-B

    print(f'#{t} {minminus}')