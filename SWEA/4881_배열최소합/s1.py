import sys
sys.stdin = open("input.txt")

def find_min(row):
    global min_sum, result
    for i in range(N):
        if visited[i] == 0:
            min_sum += number[row][i]
            if min_sum >= result:
                min_sum -= number[row][i]
                continue
            visited[i] = 1
            if row != N-1:
                find_min(row + 1)
            else:
                result = min(result, min_sum)
            min_sum -= number[row][i]
            visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    min_sum = 0
    result = 1000000000
    find_min(0)
    print("#{} {}".format(tc+1, result))