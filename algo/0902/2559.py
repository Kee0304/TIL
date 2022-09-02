N,K=map(int,input().split())
numlist=list(map(int,input().split()))

maxsum=0
for i in range(K):
    maxsum+=numlist[i]

ksum=maxsum
for j in range(1, N-K+1):
    ksum-=numlist[j-1]
    ksum+=numlist[j+K-1]
    if ksum>maxsum:
        maxsum=ksum

print(maxsum)


