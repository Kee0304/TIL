T,N=map(int,input().split())
waylist=list(map(int,input().split()))      # 한 줄로 입력되는 길들을 일단 리스트로 저장

nodeac=len(set(waylist))                    # set을 통해 노드의 개수를 구함
waymat = [[] for _ in range(N)]             # 길들을 나누어 저장할 변수

for i in range(N):
    waymat[i].append(waylist[2*i])          # 리스트에서
    waymat[i].append(waylist[2*i+1])        # 2개씩 끊어서 넣어준다.

adjlist=[[] for _ in range(nodeac)]         # 각 인덱스랑 맞추어 인접한 노드를 저장해줄 거다.

for i in range(N):
    adjlist[waymat[i][0]].append(waymat[i][1])          # 인접한 지점을 저장해주는데 이 경우는 순서=화살표 방향이라 반대를 저장해 줄 필욘 없다.


def findway(v):
    top=-1
