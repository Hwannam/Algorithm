import sys
from itertools import combinations

N = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

index_list = [i for i in range(N)]
half = list(combinations(index_list, N//2))

result = 1000000
for idx in range(len(half) // 2):
    team1 = 0
    team2 = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            a = half[idx][i]
            b = half[idx][j]
            c = half[-idx-1][i]
            d = half[-idx-1][j]
            team1 += S[a][b] + S[b][a]
            team2 += S[c][d] + S[d][c]
    result= min(abs(team1 - team2), result)
    if result == 0:
        break
print(result)