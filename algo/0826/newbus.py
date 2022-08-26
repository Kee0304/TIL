import sys
sys.stdin=open('sample_in.txt')


T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=[]
    for _ in range(N):
        lst.append(list(map(int,input().split())))

    maxstop=max([lst[0][2],lst[1][2],lst[2][2]])
    stop=[0]*(maxstop+1)

    for i in range(N):
        if lst[i][0]==1:
            for j in range(lst[i][1],lst[i][2]+1):
                stop[j]+=1

        elif lst[i][0]==2:
            for k in range(lst[i][1],lst[i][2]+1,2):
                stop[k]+=1
            
            stop[lst[i][2]]+=1
        
        elif lst[i][0]==3:
            if lst[i][1]%2==0:
                for m in range(lst[i][1],lst[i][2]+1):
                    if m%4==0:
                        stop[m]+=1
                if lst[i][2]%4!=0:
                    stop[lst[i][2]]+=1

            elif lst[i][1]%2!=0:
                for n in range(lst[i][1],lst[i][2]+1):
                    if n%3==0 and n%10!=0:
                        stop[n]+=1
                if lst[i][2]%3==0 and lst[i][2]%10!=0:
                    pass
                else:
                    stop[lst[i][2]]+=1

    print(f'#{t} {max(stop)}')

