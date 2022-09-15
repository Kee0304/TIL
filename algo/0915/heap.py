#import heapq

T=int(input())

for t in range(1,T+1):
    N=int(input())                      # 자연수 개수이자 마지막 노드의 수
#    heap=list(map(int,input().split())) # 인풋을 힙으로 사용할 거다.
#    heapq.heapify(heap)                 # 힙으로 변환
#    heap=[0]+heap                       # 인덱스를 맞춰주기 위해 더미 하나 추가
#    sum=0                               # 조상들의 합을 저장할 변수
#    idx=N                               # 시작 인덱스(마지막 노드)
#    while idx>=2:                       # 인덱스가 2보다 클 때까지만
#        idx=idx//2                      # 인덱스를 2로 나눈 몫을 인덱스로 저장
#        sum+=heap[idx]                  # 힙에서 그 인덱스에 해당하는 놈을 합에 더해줌

    heap=list(map(int,input().split())) # 인풋을 힙으로 사용할 거다.
    heap=[0]+heap                       # 인덱스를 맞춰주기 위해 더미 하나 추가
    for idx in range(2, len(heap)):
        while idx>=2:
            if heap[idx]<heap[idx//2]:  # 자기 부모와 비교해서 부모가 더 크면
                heap[idx],heap[idx//2]=heap[idx//2],heap[idx] # 교체
            idx=(idx//2)
    
    sum=0
    
    nidx=N
    while nidx>=2:
        nidx=(nidx//2)  
        sum+=heap[nidx] # 조상들 다 더해줌

    print(f'#{t} {sum}')