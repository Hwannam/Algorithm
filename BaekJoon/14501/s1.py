import sys

def work(idx, current):
    global result
    for i in range(idx, N):
        if i + info[i][0] - 1 < N:
            current += info[i][1]
            if i + info[i][0] < N:
                work(i+info[i][0], current)
            else:
                result = max(result, current)
            current -= info[i][1]
        else:
            result = max(result, current)

N = int(sys.stdin.readline().strip())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
work(0,0)
print(result)