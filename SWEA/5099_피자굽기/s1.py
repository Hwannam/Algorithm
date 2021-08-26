import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    queue = []
    for i in range(N):
        queue.append([i, Ci[i]])
    idx = N
    while len(queue) > 1:
        queue[0][1] //= 2
        if queue[0][1] == 0:
            queue.pop(0)
            if idx != M:
                queue.append([idx, Ci[idx]])
                idx += 1
        else:
            queue.append(queue.pop(0))
    print("#{} {}".format(tc+1, queue[0][0] + 1))
