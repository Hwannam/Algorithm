import sys
sys.stdin = open('input.txt')
from itertools import permutations

T = int(input())
for tc in range(T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    route_list = list(permutations([i for i in range(1, N)], N-1)) # 모든 순열
    result = 10000000
    for route in route_list:
        temp = 0
        start = 0
        for i in range(N-1):
            temp += battery[start][route[i]] # 시작 도착
            start = route[i]
        temp += battery[start][0] # 마지막
        result = min(result, temp)
    print("#{} {}".format(tc+1, result))