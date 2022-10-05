def palindrome(lst, m):                              # 2차원 배열에서 길이 m인 회문이 존재하는지 판별하는 함수
    for row in lst:                                  # 행에 대해서 탐색
        for i in range(100 - m + 1):                 # 회문 길이에 대해 가능한 시작지점들(회문 길이가 99면 range(2)로 0과 1만 탐색)
            for l in range(m // 2):                  # 회문의 길이 m을 2로 나눈 몫에 대해 1씩 늘려가며 차례대로 탐색해간다.
                if row[i + l] != row[i + m - 1 - l]: # 시작지점+l과 시작지점+회문길이-1-l이 같지 않으면
                    break                            # 루프 종료
            else:                                    # for문이 break 되지 않았으면
                return True                          # True, 즉 길이 m의 회문이 존재함
    return False                                     # for문이 도중에 break 됐으면 길이 m의 회문이 존재하지 않음


def garo(lst):                                       # 가로 회문 탐색
    max_v = 1                                        # 최대 길이를 저장할 변수
    for m in range(1, 101):                          # m에 대해
        if m > max_v + 2:                            # 만약 m이 현재 최대 길이+2보다 크면=길이가 max_v+2인 회문이 존재하지 않았다면
            return max_v                             # 현재 최대 길이를 반환
        if palindrome(lst, m):                       # 만약 길이 m의 회문이 존재하면
            max_v = m                                # 최대 길이를 갱신
    return max_v                                     # 최대 길이를 반환


def sero(lst, max_v):                                # 세로 탐색
    max_h = max_v                                    # 가로 탐색을 먼저 끝낸 후로, 시작 최대 길이는 가로최대길이. 그 아래는 찾아도 의미 없음
    for m in range(max_v, 101):
        if m > max_h + 2:
            return max_h
        if palindrome(lst, m):
            max_h = m
    return max_h


T = 10
for _ in range(1, T + 1):
    t = int(input())
    lst = [input() for _ in range(100)]
    # zip으로 전치 행렬 생성
    lst2 = list(zip(*lst))

    max_v = garo(lst2)

    if max_v != 100:                                 # 가로에서 찾은 회문의 길이가 100이면 더 탐색할 필요 없음
        max_h = sero(lst, max_v)

    result = max(max_v, max_h)
    print(f'#{t} {result}')