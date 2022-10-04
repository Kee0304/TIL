import sys
from pprint import pprint

sys.stdin=open('sample_input.txt')

def hori(row,col):
    if ((fivetree[row][col-1]=='o' and fivetree[row][col-2]=='o' and fivetree[row][col-3]=='o' and fivetree[row][col-4]=='o') or
    (fivetree[row][col+1]=='o' and fivetree[row][col+2]=='o' and fivetree[row][col+3]=='o' and fivetree[row][col+4]=='o')):
        return True

def verti(row,col):
    if ((fivetree[row-1][col]=='o' and fivetree[row-2][col]=='o' and fivetree[row-3][col]=='o' and fivetree[row-4][col]=='o') or
    (fivetree[row+1][col]=='o' and fivetree[row+2][col]=='o' and fivetree[row+3][col]=='o' and fivetree[row+4][col]=='o')):
        return True

def diag(row,col):
    if ((fivetree[row-1][col-1]=='o' and fivetree[row-2][col-2]=='o' and fivetree[row-3][col-3]=='o' and fivetree[row-4][col-4]=='o') or
    (fivetree[row-1][col+1]=='o' and fivetree[row-2][col+2]=='o' and fivetree[row-3][col+3]=='o' and fivetree[row-4][col+4]=='o') or
    (fivetree[row+1][col-1]=='o' and fivetree[row+2][col-2]=='o' and fivetree[row+3][col-3]=='o' and fivetree[row+4][col-4]=='o') or
    (fivetree[row+1][col+1]=='o' and fivetree[row+2][col+2]=='o' and fivetree[row+3][col+3]=='o' and fivetree[row+4][col+4]=='o')):
        return True

def omok(N):
    for row in range(4,4+N):
        for col in range(4,4+N):
            if fivetree[row][col]=='o':    
                if hori(row,col) == True or verti(row,col) == True or diag(row,col) == True:
                    return True

T=int(input())

for t in range(1,T+1):
    N=int(input())

    fivetree=[['.']*(4+N+4) for _ in range(4)]+[['.']*4 + list(input()) +['.']*4 for _ in range(N)]+[['.']*(4+N+4) for _ in range(4)]
    
    
    if omok(N)==True:
        print(f'#{t} YES')

    else:
        print(f'#{t} NO')
    