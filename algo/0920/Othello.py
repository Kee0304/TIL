from pprint import pprint
import sys
sys.stdin = open('sample_input(1).txt')

T=int(input())

for t in range(1,T+1):
    N,M=map(int,input().split())
    othello=[[0]*N for _ in range(N)]
    pprint(othello)

    for _ in range(M):
        row,col,bw=map(int,input().split())
        row-=1
        col-=1
        print(row,col,bw)
        # 흑돌 놓기 
        if bw==1:         
            othello[row][col]=1
                    
    

    print(othello)