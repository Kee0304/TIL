def comb(idx,r,res):
    if len(res) == r:
        tmp=tuple(res[:])
        comblist.append(tmp)
        return

    start=0

    if res:
        for idx in range(len(arr)):
            start = idx+1

    for i in range(start, len(arr)):
        res.append(arr[i])
        comb(idx+1,r,res)
        res.pop()

comblist=[]
arr=[1,2,3,3,4,5]
comb(0,3,[])
print(comblist)
#arr은 임의의 배열