from pprint import pprint
import sys
sys.stdin=open('in1.txt')

T=int(input())

def crosskill(mat,N,M):
    maxkill=0
    for row in range(N,2*N+1):
        for col in range(N,2*N+1):
            kill=0
            kill+=mat[row][col]
            for i in range(1,M):
                kill+=mat[row-i][col]
                kill+=mat[row][col+i]
                kill+=mat[row+i][col]
                kill+=mat[row][col-i]
            if kill>maxkill:
                maxkill=kill
    
    return maxkill


def diagkill(mat,N,M):
    maxkill=0
    for row in range(N,2*N+1):
        for col in range(N,2*N+1):
            kill=0
            kill+=mat[row][col]
            for i in range(1,M):
                kill+=mat[row-i][col-i]
                kill+=mat[row-i][col+i]
                kill+=mat[row+i][col-i]
                kill+=mat[row+i][col+i]

            if kill>maxkill:
                maxkill=kill
    
    return maxkill



for t in range(1,T+1):
    N,M=map(int,input().split())
    mat=[]
    for _ in range(N-1):
        mat.append([0]*(3*N-2))
    for _ in range(N):
        mat.append([0]*(N-1)+list(map(int,input().split()))+[0]*(N-1))
    for _ in range(N-1):
        mat.append([0]*(3*N-2))

    cross=crosskill(mat,N,M)
    diag=diagkill(mat,N,M)

    if cross>=diag:
        print(f'#{t} {cross}')
    else:
        print(f'#{t} {diag}')