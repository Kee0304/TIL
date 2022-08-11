import sys

sys.stdin=open("sample_input(1).txt",'r')



T=int(input())

def Subset(arr):                         # 비트 연산자를 통한 부분집합 생성
    n=len(arr)
    subset=[]
    for i in range(1<<n):
        temp=[]
        for j in range(n):                  
            if i & (1<<j):                  
                temp.append(arr[j])         
    
        subset.append(temp)

    return subset

def listsum(a):                         # 리스트 원소의 합을 반환하는 함수
    listsum=0
    for i in a:
        listsum+=i
    
    return listsum

for t in range(1, T+1):
    N,K=map(int,input().split())

    A=list(range(1,13))                 # 항상 1부터 12까지의 집합
    Asubset=Subset(A)                   # 그 부분집합을 생성                  
    cnt=0                               # 조건을 만족하는 부분집합의 개수를 셀 거다.

    for sub in Asubset:
        if len(sub)==N and listsum(sub)==K:
            cnt+=1

    print(f'#{t} {cnt}')