import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(map(int, sys.stdin.readline().split()))
robots = deque(0 for _ in range(N))
cnt = 1
while True:
    A.rotate()
    robots.rotate()
    robots[-1] = 0

    for i in range(N-2,-1,-1):
        if robots[i] == 1 and A[i+1] >= 1 and robots[i+1] == 0:
            A[i+1] -= 1
            robots[i+1] = robots[i]
            robots[i] = 0
    robots[-1] = 0

    if A[0] > 0:
        robots[0] = 1
        A[0] -= 1

    if A.count(0) >= K:
        break
    cnt += 1
print(cnt)