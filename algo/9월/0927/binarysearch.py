def leftsearch(lst,target):
    print(lst)
    if len(lst) !=0:
        if len(lst) == 1:
            if lst[0] == target:
                return 1
        elif len(lst)>=2:
            mid=(lst[0]+lst[-1])//2
            if lst[mid]==target:
                return 1
            
            else:
                return rightsearch(lst[mid+1:],target)
    return

def rightsearch(lst,target):
    print(lst)
    if len(lst) !=0:
        if len(lst) == 1:
            if lst[0] == target:
                return 1
        elif len(lst)>=2:
            mid=(lst[0]+lst[-1])//2
            if lst[mid]==target:
                return 1
            
            else:
                return leftsearch(lst[:mid],target)
    return



T = int(input())

for t in range(1,T+1):
    lena,lenb=map(int,input().split())
    alist=sorted(list(map(int,input().split())))
    blist=sorted(list(map(int,input().split())))
    cnt=0
    middle = (alist[0]+alist[-1])//2
    for num in blist:
        if alist[middle] > num:
            print(f'{alist[middle]} > {num}')
            res=leftsearch(alist[:middle],num)
            if res == 1:
                cnt+=1
        elif alist[middle] == num:
            print(f'alist[middle] == {num}')
            cnt+=1
        
        elif alist[middle] < num:
            print(f'{alist[middle]} < {num}')
            res=rightsearch(alist[middle+1:],num)
            if res == 1:
                cnt +=1
        
    print(f'#{t} {cnt}')

