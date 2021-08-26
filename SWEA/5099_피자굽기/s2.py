import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Cheese = list(map(int, input().split()))
    Ci = [0 for _ in range(M)]

    for num in range(5):
        for i in range(M):
            if 2**num <= Cheese[i] < 2**(num+1):
                Ci[i] = [i, num+1]

    idx = N
    while len(Ci) > 1:
        i = 0
        while i < idx:
            Ci[i][1] -= 1
            if Ci[i][1] == 0:
                Ci.pop(i)
                if len(Ci) < N:
                    idx -= 1
            i += 1
            print(Ci)
    print("#{} {}".format(tc+1, Ci[0][0] + 1))
