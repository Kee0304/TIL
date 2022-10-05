import sys
sys.stdin=open('input.txt')

T= int(input())

def sudoku(mat,N):

    for row in mat:                                     # 1. 행들에 1부터 9까지 중복없이 들어가있는가?
        if set(row)!=set(range(1,N+1)):
            return 0

    for row in range(N):                                # 2. 행의 합이 45인가?
        rowsum=0
        for col in range(N):
            rowsum+=mat[row][col]
        
        if rowsum!=45:
            return 0


    for col in range(N):                                # 3. 열들에 1부터 9까지 중복없이 들어가 있는가?
        collist=[]
        for row in range(N):
            collist.append(mat[row][col])
        if set(collist)!=set(range(1,N+1)):
            return 0

    for col in range(N):                                # 4. 열의 합이 45인가?
        colsum=0
        for row in range(N):
            colsum+=mat[col][row]
        
        if colsum!=45:
            return 0

    for row in range(0,N,3):                            # 5. 정사각형 안에 1~9가 중복없이 들어가있는가?
        for col in range(0,N,3):                            
            squarelist=[]                                         
            for i in range(3):                              
                for j in range(3):                          
                    squarelist.append(mat[row+i][col+j])

            if set(squarelist)!=set(range(1,N+1)):
                return 0


    for row in range(0,N,3):                            # 6. 정사각형의 합이 45인가?
        for col in range(0,N,3):                            
            squaresum=0                                          
            for i in range(3):                              
                for j in range(3):                          
                    squaresum+=mat[row+i][col+j]

            if squaresum!=45:
                return 0
            
    return 1



for t in range(1,T+1):
    N=9
    mat=[]
    for _ in range(N):
        mat.append(list(map(int,input().split())))

    print(f'#{t} {sudoku(mat,9)}')