import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    A, B = input().split()
    result = A.count(B)
    result += len(A) - (result * len(B))
    print("#{} {}".format(tc+1, result))