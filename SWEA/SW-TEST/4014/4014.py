# [SWEA / 모의 SW 역량테스트] 4014. 활주로 건설

# import sys
# sys.stdin = open('sample_input.txt')


def find_runway(arr, N, X):
    """
    지형 정보를 받아 활주로 건설 가능 여부를 확인하는 함수

    활주로는 높이가 동일한 구간에서 건설 가능하며,
    높이가 다른 구간일 경우 경사로를 설치해야 함
    """

    # 경사로 중복 설치 여부를 판별할 리스트
    visited = [False] * N
    
    for i in range(N - 1):
        # 1. 다음 지형과 높이가 똑같다면
        if arr[i] == arr[i + 1]:
            # 계속 진행
            continue
        
        # 2. 다음 지형의 높이가 1 낮다면
        if arr[i] - arr[i + 1] == 1:
            # 경사로를 설치할 높이의 기준은 arr[i + 1]
            height = arr[i + 1]
            
            # 경사로를 설치할 수 있는 범위는 i + 1 부터 i + X 까지
            for j in range(i + 1, i + 1 + X):
                # 경사로가 지형 밖을 벗어난다면
                if j >= N:
                    # 활주로를 설치할 수 없다
                    return False

                # 경사로의 높이가 연속되지 않거나 이미 경사로가 설치되어 있다면
                if arr[j] != height or visited[j]:
                    # 마찬가지로 활주로를 설치할 수 없다
                    return False
            
            # 위의 for 문을 통과하였다면, 경사로 설치 여부를 기록
            for j in range(i + 1, i + 1 + X):
                visited[j] = True
        
        # 3. 다음 지형의 높이가 1 높다면
        elif arr[i + 1] - arr[i] == 1:
            # 경사로를 설치할 높이의 기준은 arr[i]
            height = arr[i]
            
            for j in range(i - X + 1, i + 1):
                if j < 0:
                    return False

                if arr[j] != height or visited[j]:
                    return False
            
            for j in range(i - X + 1, i + 1):
                visited[j] = True
        
        # 4. 다음 지형과의 높이 차이가 1 초과 또는 1 미만이라면
        else:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    # 지도의 한 변의 크기 N, 경사로의 길이 X
    N, X = map(int, input().split())

    # 지형 정보
    road = [list(map(int, input().split())) for _ in range(N)]

    # 열 순회를 하는 대신, 주어진 지형 정보를 전치하여 전치된 배열을 행 순회
    transposed_road = list(map(list, zip(*road)))

    # 가능한 활주로의 수
    result = 0

    for r in range(N):
        if find_runway(road[r], N, X):
            result += 1
    
        if find_runway(transposed_road[r], N, X):
            result += 1
    
    print(f'#{tc} {result}')