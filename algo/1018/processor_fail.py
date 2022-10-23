from pprint import pprint

def proc(arr,N):
    for row in range(N):
        for col in range(N):
            deltalength=[]
            if arr[row][col] == 1:
                if row == 0 or row == N-1 or col == 0 or col == N-1:
                    pass
                    
                else:
                    for lcol in range(0,col):
                        if arr[row][lcol] == 1 or arr[row][lcol] ==2:
                            break
                    else:
                        deltalength.append(col)
                    
                    for rcol in range(col+1,N):
                        if arr[row][rcol] == 1 or arr[row][rcol] == 2:
                            break
                    
                    else:
                        deltalength.append(N-1-col)
                    
                    for urow in range(0,row):
                        if arr[urow][col] == 1 or arr[urow][col] ==2:
                            break
                    
                    else:
                        deltalength.append(row)
                    
                    for drow in range(row+1,N):
                        if arr[drow][col] == 1 or arr[drow][col] == 2:
                            break
                    
                    else:
                        deltalength.append(N-1-row)
                    
                    if deltalength:
                        if min(deltalength) == col:
                            for lcol in range(0,col):
                                arr[row][lcol]=2

                        elif min(deltalength) == N-1-col:
                            for rcol in range(col+1,N):
                                arr[row][rcol]=2

                        elif min(deltalength) == row:
                            for urow in range(0,row):
                                arr[urow][col]=2

                        elif min(deltalength) == N-1-row:
                            for drow in range(row+1,N):
                                arr[drow][col] = 2

                    else:
                        pass
                    



T = int(input())

for t in range(1,T+1):
    N = int(input())
    inmat = [list(map(int,input().split())) for _ in range(N)]
    proc(inmat,N)

    pprint(inmat, width=100)