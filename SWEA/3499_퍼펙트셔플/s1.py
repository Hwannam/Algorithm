import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    card = list(input().split())
    if N % 2 == 0:
        divide = N // 2
    else:
        divide = N // 2 + 1
    result = []
    for i in range(divide):
        result.append(card[i])
        if i == divide - 1 and N % 2 != 0:
            break
        result.append(card[divide+i])
    print("#{}".format(tc+1), *result)