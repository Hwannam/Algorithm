import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    nums = []
    for i in range(N): # Ai * Aj
        for j in range(i+1, N):
            a = A[i] * A[j]
            nums.append(A[i] * A[j])

    max_num = 0
    for num in nums:
        plus = True
        temp = str(num)
        for i in range(len(temp)-1):
            if int(temp[i]) > int(temp[i+1]):
                plus = False
                break
        if plus:
            if max_num < int(num):
                max_num = int(num)
    print("#{} {}".format(tc+1, max_num))