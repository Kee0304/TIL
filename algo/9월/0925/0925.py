def permu(i,r):
    global perm
    if i == r:
        tmp=bit[:]
        perm.append(tmp)
        return
    else:
        for n in arr:
            if n not in bit:
                bit[i]=n
                permu(i+1,r)
                bit[i]=None

def comb(idx,r,res):
    if len(res) == r:
        tmp=tuple(res[:])
        combset.add(tmp)
        return

    start=0

    if res:
        for idx,num in enumerate(arr):
          if num == max(res):
            start = idx+1

    for i in range(start, N):
        res.append(arr[i])
        comb(idx+1,r,res)
        res.pop()

N=5
arr=[1,3,4,6,7]
bit=[0]*N
perm=[]
combset=set()
for l in range(3):
    comb(0,l,[])

print(combset)
