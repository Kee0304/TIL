from pprint import pprint


T = int(input())

for t in range(1, T+1):
    batmat=[[0]*10 for _ in range(10) ]
    M, A = map(int,input().split())
    amove = list(map(int,input().split()))
    bmove = list(map(int,input().split()))
