import sys
sys.stdin=open('in1.txt')

T=int(input())

def crosskill(mat,N,M):
    maxkill=0
    for row in range(N):
        for col in range(N):
            kill=0
            kill+=mat[row][col]
            for i in range(1,M):
                if row-i>=0:
                    kill+=mat[row-i][col]
                
                if col+i<=N-1:
                    kill+=mat[row][col+i]
                
                if row+i<=N-1:
                    kill+=mat[row+i][col]
                
                if col-i>=0:
                    kill+=mat[row][col-i]
            if kill>maxkill:
                maxkill=kill
    
    return maxkill


def diagkill(mat,N,M):
    maxkill=0
    for row in range(N):
        for col in range(N):
            kill=0
            kill+=mat[row][col]
            for i in range(1,M):
                if row-i>=0 and col-i>=0:
                    kill+=mat[row-i][col-i]
                if row-i>=0 and col+i<=(N-1):
                    kill+=mat[row-i][col+i]
                if row+i<=(N-1) and col-i>=0:
                    kill+=mat[row+i][col-i]
                if row+i<=(N-1) and col+i<=(N-1):
                    kill+=mat[row+i][col+i]
            if kill>maxkill:
                maxkill=kill
    
    return maxkill



for t in range(1,T+1):
    N,M=map(int,input().split())
    mat=[]
    for _ in range(N):
        mat.append(list(map(int,input().split())))

    cross=crosskill(mat,N,M)
    diag=diagkill(mat,N,M)

    if cross>=diag:
        print(f'#{t} {cross}')
    else:
        print(f'#{t} {diag}')