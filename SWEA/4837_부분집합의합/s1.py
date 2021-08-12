import sys
sys.stdin = open("input.txt")

arr = [num for num in range(1, 13)]
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    n = len(arr)

    result = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        if len(temp) == N and sum(temp) == K:
            result += 1

    print("#{} {}".format(tc+1, result))