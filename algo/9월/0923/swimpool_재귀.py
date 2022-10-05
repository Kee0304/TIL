import sys

sys.stdin=open('sample_input.txt')

def fee(month, accfee):
    global minfee
    if month>12:            # 12월이 지났을 때
        if accfee < minfee: # 현재 누적 비용이 최소 비용보다 작으면
            minfee = accfee # 최소 비용에 저장
        return              # 끝
    
    if swimplan[month]:     # 이용 계획이 존재하면
        for i in range(4):  # 1일, 1달, 3달, 1년에 대해 탐색
            if i == 0:
                fee(month+1,accfee+feelist[i]*swimplan[month])  # 1일 요금으로 1달 이용
            elif i == 1: 
                fee(month+1,accfee+feelist[i])                  # 1달 요금으로 1달 이용
            elif i == 2:
                fee(month+3, accfee+feelist[i])                 # 3달 요금으로 3달 이용
            elif i == 12:
                fee(month+12, accfee+feelist[i])                # 1년 요금으로 1년 이용
    else:                   # 이용 계획이 없으면
        fee(month+1,accfee) # 다음 달로

T=int(input())

for t in range(1,T+1):
    feelist=list(map(int,input().split()))
    swimplan=[0]+list(map(int,input().split()))
    minfee=feelist[3]   # 일단 1년 금액을 최소 금액으로 저장
    month=1             # 시작 달
    accfee=0            # 누적 금액
    fee(month,accfee)
    print(f'#{t} {minfee}')