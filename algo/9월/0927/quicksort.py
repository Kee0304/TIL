def quicksort(lst,l,r):
    if l<r:
        pivot=lomuto(lst,l,r)       # lomuto 분할로 분할
        quicksort(lst,l,pivot-1)    # 왼쪽 퀵소트
        quicksort(lst,pivot+1,r)    # 오른쪽 퀵소트
    
def lomuto(lst,l,r):                    # lomuto 분할
    pivot=lst[r]                        # 오른쪽 끝이 피벗
    i=l-1                               # 첫 인덱스는 l=1로
    for j in range(l,r):                # l부터 r까지 돌면서
        if lst[j]<=pivot:               # lst[j]가 피벗보다 작으면
            i+=1                        # i를 하나 올리고
            lst[i],lst[j]=lst[j],lst[i] # 교환. 즉 피벗보다 작은 놈들만 나왔을 때는 자기 자신을 교환
                                        # 만약 피벗보다 큰 값이 나왔으면 j는 for이라 계속 증가하지만
                                        # i는 증가하지 않고 자리 바꿈도 없다.
                                        # 다시 피벗보다 작은 놈을 만나기 전까지 i는 그대로이다가
                                        # 피벗보다 작은 놈을 만나면 i가 하나 커지고 j 자리와 교환

    lst[r],lst[i+1] = lst[i+1],lst[r]   # 피벗을 i+1에 넣고 거기 있던 놈은 오른쪽 끝으로
    return i+1                          # i+1이 분할의 기준점이 된다.

T = int(input())

for t in range(1,T+1):
    N=int(input())
    inlst=list(map(int,input().split()))
    quicksort(inlst,0,N-1)

    print(f'#{t} {inlst[N//2]}')