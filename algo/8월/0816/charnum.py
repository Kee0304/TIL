import sys
sys.stdin=open('sample_input(2).txt')

T=int(input())

for t in range(1,T+1):
    strlist=[]                      # 입력받은 문자열을 2줄씩 나누어서 입력받음.
    for _ in range(0,2):
        strlist.append(list(input()))
    
    cntlist=[0]*len(strlist[0])     # 각 문자가 str2에 존재하는 개수를 저장할 리스트
    for i in range(len(strlist[0])):
        cnt=0                       # 문자 개수가 저장될 변수
        for j in strlist[1]:
            if strlist[0][i]==j:    # str2를 탐색해서 str1의 문자가 하나 존재할 때 마다
                cnt+=1              # 개수를 하나씩 늘려주고
        cntlist[i]=cnt              # 그 개수를 저장해준다.
        
    print(f'#{t} {max(cntlist)}')