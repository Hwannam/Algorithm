import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    A, B = input().split()
    result = 0
    length = len(B)
    i = 0
    while i < len(A) - length + 1:
        if A[i:i + length] == B:
            result += 1
            i += length
        else:
            i += 1
    result += len(A) - (result * len(B))
    print("#{} {}".format(tc+1, result))