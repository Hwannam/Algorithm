import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    list_ai = list(map(int, input().split()))
    max = min = list_ai[0]

    for ai in list_ai:
        if max < ai:
            max = ai
        elif min > ai:
            min = ai
    result = max - min

    print("#{} {}".format(tc+1, result))