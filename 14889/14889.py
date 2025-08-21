import sys
import itertools

# sys.stdin = open('input.txt')


def calculate_ability(member, ability):
    """
    각 팀의 능력치 합을 계산하는 함수
    """
    ability_sum = 0

    # 팀원 리스트를 순회하며 능력치를 더한다
    for i in member:
        for j in member:
            ability_sum += ability[i][j]
    
    return ability_sum


# 축구를 하기 위해 모인 사람 N
N = int(input())

# 인덱스를 통해 각 사람을 나타내는 리스트 생성
people = []

for i in range(N):
    people.append(i)

# 능력치를 담은 N * N 크기의 배열 ability
ability = [list(map(int, input().split())) for _ in range(N)]

# 팀별 능력치 차이를 저장할 리스트 초기화
difference = []

# N명 중 N/2명을 뽑는 경우의 수
teams = itertools.combinations(people, N // 2)

for team_start in teams:
    # 팀원의 중복을 제거하기 위해 set 차집합 사용
    team_link = list(set(people) - set(team_start))

    # 함수를 통한 각 팀의 능력치 합계 계산
    start_ability = calculate_ability(team_start, ability)
    link_ability = calculate_ability(team_link, ability)

    # 능력치 차이를 절댓값으로 구함
    difference.append(abs(start_ability - link_ability))

# 스타트 팀과 링크 팀의 능력치 차이의 최솟값 출력
print(min(difference))