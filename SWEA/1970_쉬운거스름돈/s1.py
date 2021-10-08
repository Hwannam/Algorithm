import sys
sys.stdin = open("input.txt")

T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(T):
    N = int(input())
    print("#{}".format(tc+1))
    for money in money_list:
        money_cnt = N // money
        print('{}'.format(money_cnt), end = " ")
        N -= money_cnt * money
    print()