import sys

sys.stdin=open("sample_input(2).txt",'r')


T=int(input())
                                                           # 처음엔 실시간으로 먼저 도달한 놈이 이기게 하려고 했는데, 조금 어려워서
def binarySerachCount(a,N,key):                            # 그냥 2진 탐색을 한 횟수를 비교할 거다.
    start=0
    end=N-1
    cnt=0
    while start<end:
        middle = (start+end)//2
        if a[middle]==key:
            cnt+=1
            return cnt
        elif a[middle]>key:
            end = middle
            cnt+=1
        else:
            start = middle
            cnt+=1



for t in range(1,T+1):                                      
    P,A,B=map(int,input().split())

    acnt=binarySerachCount(list(range(1,P+1)),P,A)      # A와 B에 대해 2진 탐색 횟수를 저장하고
    bcnt=binarySerachCount(list(range(1,P+1)),P,B)

    if acnt<bcnt:                                       # 이를 비교하여 작은 놈이 이긴다.
        print(f'#{t} A')
    elif acnt>bcnt:
        print(f'#{t} B')
    elif acnt==bcnt:
        print(f'#{t} 0')