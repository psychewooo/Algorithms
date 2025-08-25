import sys

sys.stdin = open('sample_input.txt')

# 총 테스트 케이스의 개수 T
T = int(input())

for test_case in range(1, T + 1):
    # 1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권의 요금
    charge = list(map(int, input().split()))

    # 1월부터 12월까지의 수영장 이용 계획
    plan = list(map(int, input().split()))

    # dp[i] = i월까지 수영장을 이용할 수 있는 최소 비용
    # dp[0] = 0: 인덱스 값과 월을 맞추기 위해 존재
    dp = [0] * 13

    # 1. 1일 이용권, 1달 이용권 둘 중 최소 금액 비교
    for i in range(1, 13):      # i = 1, 2, 3, ..., 12
        # plan[i - 1]: 해당 월의 수영장 이용 횟수
        # charge[0]: 1일 이용권의 금액
        # charge[1]: 1달 이용권의 금액
        lowest_charge = min(plan[i - 1] * charge[0], charge[1])     # 1일 이용권과 1달 이용권의 비교

        # 최소 금액 누적
        dp[i] = dp[i - 1] + lowest_charge

        # 2. 3달 이용권의 금액
        if i >= 3:
            # dp[i - 2]: 3개월 전까지의 최소 비용
            # charge[2]: 3달 이용권의 금액
            dp[i] = min(dp[i], dp[i - 3] + charge[2])    # 1번(1일 이용권과 1달 이용권 중 최소)과 3달 이용권의 비교

    # 3. 1년 이용권의 금액
    # charge[3]: 1년 이용권의 금액
    result = min(dp[12], charge[3])     # 일 년간 최소 비용과 1년 이용권 중 더 저렴한 것을 결과로 택한다

    print(f'#{test_case} {result}')