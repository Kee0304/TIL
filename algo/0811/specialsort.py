T=int(input())

def list_max(a):                                    # 최대값을 추출하는 함수
    maxnum=a[0]
    for num in a:
        if num>maxnum:
            maxnum=num
    
    return maxnum


def CountingSort(A, k):                             # 카운팅 정렬
    C=[0]*(k+1)
    B=[0]*len(A)

    for i in range(0, len(A)):
        C[A[i]]+=1
    
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    for i in range(len(B)-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    
    return B
    

for t in range(1,T+1):                      
    N=int(input())
    numlist=list(map(int,input().split()))


    cslist=CountingSort(numlist,list_max(numlist))          # 먼저 입력받은 숫자들을 리스트화한다.
    splist=[0]*len(numlist)                                 # 특별한 정렬을 한 수들을 집어넣을 리스트를 만든다.

    for i in range(0,N//2):                                 # 아래의 과정을 N//2번만큼 반복한다.
        splist[0+2*i]=cslist[-1-i]                          # 큰놈들은 큰 순서대로 0+2i 인덱스에 집어넣고
        splist[1+2*i]=cslist[0+i]                           # 작은 놈들은 작은 순서대로 1+2i 인덱스에 집어넣는다.
    
    if N%2!=0:                                              # 위 과정을 끝냈을 때 만약 N이 홀수라면 마지막 자리가 채워지지 않으므로, 정렬된 리스트의 중앙에 있는 값을 채워넣어준다.
        splist[-1]=cslist[N//2]

    result=splist[0:10]

    print(f'#{t} {" ".join(map(str,result))}')              # 리스트 요소들을 문자열로 바꾸고 리스트 전체를 띄어쓰기 기준으로 문자열로 통합해준다.
    

    