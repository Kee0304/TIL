lst=[1,2,3,4]
ans=[]

q=[[]]
tmp=q.pop(0)
for i in lst:
    tmp.append(i)
    ans.append(tmp[:])
    tmp.pop()

print(ans)

res=[]
for tmp_power_set in ans:
    for i in lst:
        if i > lst[-1]:
            tmp_power_set.append(i)
            res.append(tmp_power_set[:])
            tmp_power_set.pop()
            print(res)