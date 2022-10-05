import sys
sys.stdin=open('input.txt')

def postorder(root):                    # 트리를 후위표기법으로 변환하는 함수
    if int(ch1[root])!=0:
        postorder(ch1[root])
        postorder(ch2[root])
        resultlist.append(par[root])
    else:
        resultlist.append(par[root])
    return resultlist



for t in range(1,11):
    node=int(input())
    anlist=[[] for _ in range (node+1)]
    par=[0]*(node+1)
    ch1=[0]*(node+1)
    ch2=[0]*(node+1)
    for idx in range(1,node+1):          # 일단 리스트 형태로 저장
        inputlist=list(input().split())
        anlist[idx]=inputlist

    for idx in range(1,node+1):
        if len(anlist[idx])==4:                         # 길이가 4, 즉 자식 노드가 두 개 있으면
            par[int(anlist[idx][0])]=anlist[idx][1]     # 부모     
            ch1[int(anlist[idx][0])]=int(anlist[idx][2])# 왼쪽 자식
            ch2[int(anlist[idx][0])]=int(anlist[idx][3])# 오른쪽 자식
        elif len(anlist[idx])==2:                       # 갈아가 2, 즉 자식이 없으면
            par[int(anlist[idx][0])]=int(anlist[idx][1])
    resultlist=[]                                       # 후위표기법을 저장할 

    a=postorder(1)
    stack=[]
    for idx in range(len(a)):           #후위 표기법 계산
        if type(a[idx])==int:
            stack.append(a[idx])
        elif a[idx] == '+':
            num1=stack.pop()
            num2=stack.pop()
            stack.append(int(num2+num1))
        elif a[idx] == '-':
            num1=stack.pop()
            num2=stack.pop()
            stack.append(int(num2-num1))
        elif a[idx] == '*':
            num1=stack.pop()
            num2=stack.pop()
            stack.append(int(num2*num1))
        elif a[idx] == '/':
            num1=stack.pop()
            num2=stack.pop()
            stack.append(int(num2/num1))

    print(f'#{t} {stack.pop()}')        # 출력