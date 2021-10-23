import sys
from itertools import combinations

def find_distance(pick):
    global result
    answer = 0
    for home in house:
        temp = 2*N
        for st in pick:
            temp = min(temp, abs(home[0] - st[0]) + abs(home[1]-st[1]))
        answer += temp
    result = min(answer, result)

N,M = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
store = []
house = []
for i in range(N):
    for j in range(N):
        if info[i][j] == 2:
            store.append((i,j))
        elif info[i][j] == 1:
            house.append((i,j))

picked = list(combinations(store,M))
result = 100000
for pick in picked:
    find_distance(pick)
print(result)