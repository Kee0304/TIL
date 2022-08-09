T=int(input())

def BubbleSort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

for test_case in range(1,T+1):
    N=int(input())
    boxlist=list(map(int,(input().rstrip(" ").split(" "))))
    s_boxlist=BubbleSort(boxlist)
    n=len(s_boxlist)

    for dump in range(0,N):
        s_boxlist[0]+=1
        s_boxlist[-1]-=1
        if s_boxlist[0]>s_boxlist[1]:
            BubbleSort(s_boxlist)
        
    print(f'#{test_case} {s_boxlist[n-1]-s_boxlist[0]}')
