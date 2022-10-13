def permu(idx,r):
    global perm
    if idx == r:
        tmp=[]
        for n in range(len(bit)):
            tmp.append(bit[n][1])
        perm.append(tmp)
        return
    else:
        for i,value in enumerate(arr):
            if (i,value) not in bit:
                print(i,value)
                bit[idx]=(i,value)
                permu(idx+1,r)
                bit[idx]=None

N=int(input())
perm=[]
bit=[0]*N
arr=[1,2,3,3]
permu(0,N)
print(perm)
