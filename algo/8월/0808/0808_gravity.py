#9
#7 4 2 0 0 6 0 7 0

#N = int(input())
#mat=[]
#arr=list(map(int,input().split(' ')))
#for i in range(0,N):
#    mat.append([0*N]*N)

#for n in range(0,N):
#    for m in range(0,arr[n]):
#        mat[N-m-1][n]=1

#while n<N-1:
#    for m in range(0,N):
#        if mat[n][m]


#상자는 아래에서 부터 쌓이기 때문에, 가장 위에 있는 놈을 확인해서 오른쪽에 상자가 있다면 아래에 있는 놈들은 당연히 막혀있다.

N = int(input())
arr=list(map(int,input().split(' ')))


result=0                                       #결과를 저장할 변수

for i in range(len(arr)):
    value=arr[i]
    cnt=0                                      #나보다 작은 박스 무더기를 구해서 카운트에 더해줄 거다.

    for right in range(i+1,len(arr)):          #나보다 오른쪽 놈들이랑 비교할 거다.
        if value>arr[right]:
            cnt+=1
    
    if cnt>result:                             #만약 cnt가 현재 result보다 크면 cnt를 저장할 거다.
        result=cnt

print(result)