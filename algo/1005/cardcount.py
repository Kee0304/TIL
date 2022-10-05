T = int(input())

for t in range(1,T+1):
    instr=input()
    card=[set(),set(),set(),set()]          # 들어오는 카드들을 기호에 맞춰 set으로 저장하는 리스트

    for idx in range(0,len(instr),3):       # 3개씩 띄어서 보면 됨

        if instr[idx]=='S':                 # 기호에 맞춰서
            card[0].add((instr[idx:idx+3])) # 3개씩 저장
        elif instr[idx]=='D':
            card[1].add((instr[idx:idx+3]))
        elif instr[idx]=='H':
            card[2].add((instr[idx:idx+3]))
        elif instr[idx]=='C':
            card[3].add((instr[idx:idx+3]))
        
    cardnum=int(len(instr)/3)               # 주어지는 카드의 수
    totalcard=0                             # set으로 만든 카드의 수
    for cidx in range(4):
        totalcard+=len(card[cidx])          # 카드 수 다 더함
    
    if totalcard==cardnum:                  # 중복이 없으면
        print(f'#{t} {13-len(card[0])} {13-len(card[1])} {13-len(card[2])} {13-len(card[3])}')
    
    else:                                   # 중복이 있으면
        print(f'#{t} ERROR')