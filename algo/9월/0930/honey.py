import sys
sys.stdin=open('sample_input.txt')

def comb(idx,r,res,arr):
    global combset
    if len(res) == r:
        tmp=tuple(res[:])

        if sum(tmp)<=maxhoney:
            comblist.append(tmp)
        return

    start=0

    if res:
        for idx,num in enumerate(arr):
          if num == max(res):
            start = idx

    for i in range(start, len(arr)):
        res.append(arr[i])
        comb(idx+1,r,res,arr)
        res.pop()





T = int(input())

for t in range(1,10+1):
    N,M,C = map(int,input().split()) # 벌통의 총크기 N*N, 한 마리가 선택할 수 있는 벌통의 개수 M
                                     # 한 마리가 채취할 수 있는 꿀의 최대량 C
    inmat=[list(map(int,input().split())) for _ in range(N)]

    bees=[]
    maxhoney=C
    
    minmaxhoney=0
    partlist=[]
    for row in range(N):
        for col in range(N-M+1):
            comblist=[]
            tmp=inmat[row][col:col+M]
            for r in range(1,M+1):
                comb(0,r,[],tmp)
            for combination in comblist:
                partsqsum=0
                partsqsumlist=[]
                for i in range(len(combination)):
                    partsqsum+=(combination[i])**2
                partsqsumlist.append([partsqsum,len(combination),(row,col)])
            
                partlist.append(partsqsumlist)

    for idx in range(len(partlist)):
        partlist[idx]=partlist[idx][0]
    
    for idx in range(len(partlist)-1):
        for subidx in range(len(partlist)):
            if idx != subidx:
                if partlist[idx] and partlist[subidx]:
                    if partlist[idx][2][0]==partlist[subidx][2][0]:
                        if partlist[subidx][2][1] - partlist[idx][2][1] < M:
                            if partlist[idx][0]>=partlist[subidx][0]:
                                partlist[subidx]=None
                            else:
                                partlist[idx]=None

    no=partlist.count(None)
    for _ in range(no):
        partlist.remove(None)
    partlist.sort(reverse=True)

    print(f'#{t} {partlist[0][0]+partlist[1][0]}')
