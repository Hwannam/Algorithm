import sys
sys.stdin = open("input.txt")
from itertools import combinations

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = 200000
    for i in range(1, len(heights) + 1):
        temps = list(combinations(heights, i))
        for temp in temps:
            sum_height = sum(temp)
            if B <= sum_height < result:
                result = sum_height
        if result == B:
            break
    print("#{} {}".format(tc+1, result - B))