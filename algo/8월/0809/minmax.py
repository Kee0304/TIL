T = int(input())

def BubbleSort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

for test_case in range(1, T + 1):
    N=int(input())
    numlist=list(map(int,(input().rstrip(" ").split(" "))))
    s_numlist=BubbleSort(numlist)
    
    print(f'#{test_case} {s_numlist[-1]-s_numlist[0]}')
