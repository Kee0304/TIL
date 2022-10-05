T=int(input())

#최댓값 찾기
def maxnum(a):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    
    return a[-1]

for test_case in range(1, T+1):
    N=int(input())
    numlist=list(map(int,list(input())))

    aclist=[0]*(maxnum(numlist)+1)  #카운팅 정렬과 비슷하게 숫자=인덱스로 누적 리스트를 만들 것이다. 주어진
    maxnumber=0
    maxac=0
  

    for number in numlist:          #숫자가 나오면 해당하는 인덱스에 1씩 추가
        aclist[number]+=1
    
    rs_aclist=aclist[::-1]          #그 리스트를 거꾸로 돌려서, 같은 수면 큰 숫자가 나오도록

    for idx in range(0,len(rs_aclist)):         #계속 탐색하면서 max값과 그 개수를 반환 
        if rs_aclist[idx]>maxac:
            maxnumber=maxnum(numlist)-idx
            maxac=rs_aclist[idx]
    
    print(f'#{test_case} {maxnumber} {maxac}')


