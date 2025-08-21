### 14889 스타트와 링크
**결과**
1. 런타임 에러 (FileNotFoundError)
2. 시간 초과  


```python
def select_team(N):

    teams = []

    for member_start in itertools.combinations(people, int(N/2)):
        team_start = set(member_start)
        team_link = set(people) - team_start
    
        sorted_teams = tuple(sorted([list(team_start), list(team_link)]))

        if sorted_teams not in teams:
            teams.append(sorted_teams)

    return teams


def calculate_ability(member, ability):

    ability_sum = 0

    for i in member:
        for j in member:
            ability_sum += ability[i][j]
    
    return ability_sum


N = int(input())

people = []

for i in range(N):
    people.append(i)

ability = [list(map(int, input().split())) for _ in range(N)]

difference = []

for two_teams in select_team(N):
    start_member = two_teams[0]
    link_member = two_teams[1]

    start_ability = calculate_ability(start_member, ability)
    link_ability = calculate_ability(link_member, ability)

    difference.append(abs(start_ability - link_ability))

print(min(difference))
```
**해결 방안**
1. 백준 사용이 처음이라 양식 오류로 인한 런타임 에러 발생
2. select_team 함수를 제거하고 메인 코드 블록에 itertools.combination 직접 사용