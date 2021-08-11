import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    list_ai = list(map(int, input().split()))
    max = min = sum(list_ai[0:M])

    for i in range(1, N-M+1):
        sum_list = sum(list_ai[i:i + M])
        if max < sum_list:
            max = sum_list
        elif min > sum_list:
            min = sum_list
    print("#{} {}".format(tc+1, max-min))