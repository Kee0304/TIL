import sys

sys.stdin = open('회문2_input.txt')

def maxlength(a):
    maxlen=0
    for lst in a:
        if len(lst)>maxlen:
            maxlen=len(lst)
    
    return maxlen


for t in range(1, 11):
    test_case = int(input())
    mat = []                                                # 매트릭스 형태로 표현
    N = 100                                                 # 100줄짜리란다.
    for _ in range(N):
        mat.append(list(input()))

    maxlen=1
    strlist=['e']
    for row in range(N):
        for start_col in range(N):
            for i in range(1,N-start_col):
                numlist=[]
                for j in range(0,i+1):
                    numlist.append(mat[row][start_col+j])

                if numlist==numlist[::-1] and len(numlist)>maxlen:
                    strlist.append(numlist)
                    maxlen=len(numlist)


    for col in range(0,N):
        for start_row in range(0,N):
            for i in range(1,N-start_row):
                numlist=[]
                for j in range(0,i+1):
                    numlist.append(mat[start_row+j][col])

                if numlist==numlist[::-1] and len(numlist)>maxlen:
                    strlist.append(numlist)
                    maxlen=len(numlist)

    print(f'#{t} {maxlength(strlist)}')
    