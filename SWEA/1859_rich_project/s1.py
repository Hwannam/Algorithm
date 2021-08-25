import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    high = 0
    profit = 0
    for idx in range(N-1, -1, -1):
        if price[idx] > high:
            high = price[idx]
        else:
            profit += high - price[idx]
    print("#{} {}".format(tc+1, profit))