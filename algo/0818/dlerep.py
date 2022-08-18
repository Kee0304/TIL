import sys
sys.stdin=open('sample_input(3).txt')

T= int(input())

def delrep(a):                          # 연속되는 문자를 제거해주는 함수를 만든다.
    lista=list(a)                       # 리스트로 변환
    for i in range(len(a)-1):
        if lista[i]==lista[i+1]:        # 해당 인덱스와 다음 인덱스에 있는 문자가 같으면
            lista[i]=lista[i+1]=''      # 공백으로 변환해준다.
        
    modi_str="".join(lista)             # 그 뒤 문자열로 변환하고

    if modi_str==a:                     # 만약 변화가 없었다면 더 이상 제거할 만한 부분이 없다는 것으로 그대로 반환하고
        return modi_str
    else:                               # 변화가 있었다면 아직 안 끝났을 수도 있으므로 다시 한 번 함수를 돌려준다.
        return delrep(modi_str)

    

for t in range(1,T+1):
    inputstring=input().rstrip()

    print(f'#{t} {len(delrep(inputstring))}')