import sys
sys.stdin = open('input.txt')

def find_case(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return 2*find_case(N-20) + find_case(N-10)

T = int(input())
for tc in range(T):
    N = int(input())
    print("#{} {}".format(tc+1, find_case(N)))