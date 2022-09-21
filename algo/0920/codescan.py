hextobi={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100',
    '5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010',
    'B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}             # 16진수 -> 2진수 변환 딕셔너리

def 뒤에서부터지우기(bistr):
    global pslist                   # global로 불러옴
    global bslist                                                        
    backonecnt=0                    
    backzerocnt=0
    frontonecnt=0
    
    idx=len(bistr)-1                # 가장 끝을 인덱스로 잡는다.
    
    if idx>0:
        while bistr[idx]=='1':      # 뒤에서부터 1을 세준다.
            backonecnt+=1           # 개수 기억
            idx-=1                  # 인덱스 이동

        while bistr[idx]=='0':      # 1을 세면 언젠가 0을 만난다. 그 때부턴 0을 세준다.
            backzerocnt+=1          # 개수 기억
            idx-=1                  # 인덱스 이동

        while bistr[idx]=='1':      # 그 다음엔 또 1을 만난다. 또 세줌
            frontonecnt+=1          # 개수 기억
            idx-=1                  # 인덱스 이동

        while bistr[idx]=='0':      # 그럼 또 0을 만난다.
            idx-=1                  # 이 놈은 개수 기억 필요 없이 인덱스만 내려줌

        for i in range(min(frontonecnt,backzerocnt,backonecnt), 0, -1):     # 최대 공약수 찾아서 비율을 만들 거다.
            if frontonecnt%i==0 and backzerocnt%i==0 and backonecnt%i==0:
                r=i                                                         # 비율 저장
                break
  
        fo=int(frontonecnt/r)                                               # 기억한 개수들을 비율로 나눠서 1과 0과 1의 개수 비를 찾는다.
        bz=int(backzerocnt/r)
        bo=int(backonecnt/r)

        if (fo,bz,bo) == (2,1,1):                                           # 문제에서 제시된 비율에 따라 숫자 입력
            bslist.append(0)
        elif (fo,bz,bo) == (2,2,1):
            bslist.append(1)
        elif (fo,bz,bo) == (1,2,2):
            bslist.append(2)
        elif (fo,bz,bo) == (4,1,1):
            bslist.append(3)
        elif (fo,bz,bo) == (1,3,2):
            bslist.append(4)
        elif (fo,bz,bo) == (2,3,1):
            bslist.append(5)
        elif (fo,bz,bo) == (1,1,4):
            bslist.append(6)
        elif (fo,bz,bo) == (3,1,2):
            bslist.append(7)
        elif (fo,bz,bo) == (2,1,3):
            bslist.append(8)
        elif (fo,bz,bo) == (1,1,2):
            bslist.append(9)

        if len(bslist) == 8 and (tuple(bslist[::-1]) not in set(pslist)):   # 만약 뒤집은 놈이 pslist에 없으면 추가
            pslist.append(tuple(bslist[::-1]))
            bslist=[]                                                       # bslist 초기화
        elif len(bslist) == 8 and (tuple(bslist[::-1]) in set(pslist)):
            bslist=[]                                                       # 초기화
        
        bistr=bistr[0:idx+1]                                                # 내린 인덱스 만큼 잘라주고

        return 뒤에서부터지우기(bistr)                                        # 다시 함수 실행

T=int(input())                                      # 테스트 케이스
for t in range(1,T+1):                              # 만큼 반복
    N,M=map(int,input().split())                    # N,M 입력 받고
    psmat=[[] for _ in range(N)]                    # 전체 배열을 입력받을 2차원 리스트
    for idx in range(N):                            
        psmat[idx]=input().strip()                  # 들어오는 놈들을 2차원 배열에 저장
   
    pslist=[]                                       # 암호 코드들을 저장할 변수
    bslist=[]                                       # 8자리 암호 코드들을 저장하고 초기화해줄 변수

    for i in range(N):
        if psmat[i]=='0'*M:                         # 00000... 인 놈들은 건너 뛴다.
            pass
        else:
            tmplst=psmat[i][:]                      # 문자열 복사
            hexlist=list(tmplst)                    # 리스트화
            for i in range(len(hexlist)):
                hexlist[i]=hextobi[hexlist[(i)]]    # 현재 16진수 문자열이므로 딕셔너리에 따라 2진수로 변환
            bistr="".join(hexlist).rstrip('0')      # 오른쪽부터 0 싹 제거
            뒤에서부터지우기(bistr)                  # 함수 실행

    result=0                                                                                                                        # 결과를 저장할 변수
    for i in range(len(pslist)):
        if ((pslist[i][0]+pslist[i][2]+pslist[i][4]+pslist[i][6])*3+(pslist[i][1]+pslist[i][3]+pslist[i][5])+pslist[i][7])%10==0:   # 문제에서 제시된 조건대로 판별해서 맞으면
            result+=pslist[i][0]+pslist[i][2]+pslist[i][4]+pslist[i][6]+pslist[i][1]+pslist[i][3]+pslist[i][5]+pslist[i][7]         # 다 더해서 결과에 더해줌
        else:
            pass
    
    print(f'#{t} {result}')
    
