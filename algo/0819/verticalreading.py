import sys
sys.stdin=open('sample_input.txt')

T=int(input())

def maxlength(mat):                                 # 길이가 맞춰진 2차원 배열과 최대 길이를 반환해줄 함수
    maxlen=0
    for lst in mat:
        if len(lst)>maxlen:
            maxlen=len(lst)
    
    for lst in mat:
        if len(lst)<maxlen:
            for _ in range(maxlen-len(lst)):        # 짧은 놈들에 None을 append 해줘서 길이를 맞추고
                lst.append(None)

    return mat,maxlen                               # 2차원 배열과 최대 길이를 튜플로 반환해준다.



for t in range(1,T+1):
    mat=[]
    N=5
    for _ in range(N):
        mat.append(list(input()))
    
    rmat=maxlength(mat)
    strlist=[]                                      # 세로로 읽은 문자열을 저장해줄 리스트

    for col in range(rmat[1]):                      # 길이가 맞춰진 2차원 배열을 열을 기준으로 최대 길이만큼 탐색해서
        for row in range(N):
            if rmat[0][row][col]!=None:             # None이 아니면 문자열 리스트에 저장해준다.
                strlist.append(rmat[0][row][col])
                


    print(f'#{t} {"".join(strlist)}')               # 합쳐서 문자열로 변환해주고 출력