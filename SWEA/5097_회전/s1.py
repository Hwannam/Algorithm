import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    if M >= N:
        M = M % N
    print("#{} {}".format(tc+1, nums[M]))