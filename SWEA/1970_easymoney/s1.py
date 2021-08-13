import sys
sys.stdin = open("input.txt")

T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(T):
    result = []
    N = int(input())
    for money in money_list:
        result.append(N // money)
        N -= (N // money) * money
    print("#{}".format(tc+1))
    print("{}".format(" ".join(map(str, result))))