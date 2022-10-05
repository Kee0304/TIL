T=int(input())
 
for t in range(1,T+1):
    N=int(input())                      # 자연수 개수이자 마지막 노드의 수
 
    heap=list(map(int,input().split())) # 인풋을 힙으로 사용할 거다.
    heap=[0]+heap                       # 인덱스를 맞춰주기 위해 더미 하나 추가
    for idx in range(2, len(heap)):
        while idx>=2:
            if heap[idx]<heap[idx//2]:
                heap[idx],heap[idx//2]=heap[idx//2],heap[idx]
            idx=(idx//2)
     
    sum=0
     
    nidx=N
    while nidx>=2:
        nidx=(nidx//2)
        sum+=heap[nidx]
 
    print(f'#{t} {sum}')