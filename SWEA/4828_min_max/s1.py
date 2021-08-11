import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    list_ai = list(map(int, input().split()))
    result = max(list_ai) - min(list_ai)

    print("#{} {}".format(tc+1, result))