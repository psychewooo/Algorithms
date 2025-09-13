# [SWEA / D3] 1244. 최대 상금

# import sys
# sys.stdin = open('input.txt')


# 함수 정의
def dfs(lst, count):
    """
    깊이 우선 탐색을 통하여
    정해진 횟수만큼 숫자판을 교환할 때
    받을 수 있는 가장 큰 금액을 계산하는 함수

    :param lst: (list) 현재 숫자판의 배열 상태
    :param count: (int) 현재까지의 숫자판 교환 횟수
    """
    # 글로벌 변수 불러오기
    global prize

    # 가지치기
    current_state = (int("".join(lst)), count)

    if current_state in visited:
        return

    # 현재 상태를 기록
    visited.add(current_state)

    # 종료 조건
    # 교환 횟수를 충족하였을 때 종료
    if count == exchange:
        # 현재까지의 값과 최대 값을 비교
        prize = max(prize, int("".join(lst)))
        return

    # 숫자판의 배열 중 두 가지 숫자 뽑기
    # for 문 통한 구현
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            # 뽑은 두 숫자의 위치를 변경한다
            lst[i], lst[j] = lst[j], lst[i]

            # 재귀 호출
            # 교환 횟수를 한 번 증가
            dfs(lst, count + 1)

            # 위치 변경하였던 숫자를 다시 원 위치
            lst[j], lst[i] = lst[i], lst[j]


# 테스트 케이스의 수 T
T = int(input())

for tc in range(1, T + 1):
    # 숫자판의 정보 arr, 교환 횟수 exchange
    input_arr, input_exchange = input().split()

    # type 'str'에서 계산을 위해 각각의 타입 변경
    arr = list(input_arr)
    exchange = int(input_exchange)

    # 금액 변수 설정
    prize = 0

    # 가지치기를 위해 중복 여부를 기록할 빈 set 생성
    visited = set()

    # DFS 탐색 시작
    # 교환을 시작하기 전 숫자판의 배열, 교환 횟수 0번
    dfs(arr, 0)

    print(f'#{tc} {prize}')