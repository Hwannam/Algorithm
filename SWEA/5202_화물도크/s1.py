import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    end_time = 0
    time.sort(key=lambda x: x[1])
    for schedule in time:
        if end_time <= schedule[0]:
            end_time = schedule[1]
            result += 1

    print("#{} {}".format(tc+1, result))
