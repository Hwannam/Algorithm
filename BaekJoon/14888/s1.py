import sys

from itertools import permutations
def calculate(calc):
    global max_result, min_result
    answer = A[0]
    for i in range(1,N):
        if calc[i-1] == '+':
            answer += A[i]
        elif calc[i-1] == '-':
            answer -= A[i]
        elif calc[i-1] == '*':
            answer *= A[i]
        elif calc[i-1] == '/':
            if answer < 0:
                temp = -1 * answer
                temp //= A[i]
                answer = -1 * temp
            else:
                answer //= A[i]
    max_result = max(answer, max_result)
    min_result = min(answer, min_result)


N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
info = list(map(int, sys.stdin.readline().split()))
signs = []
for i in range(info[0]):
    signs.append('+')
for i in range(info[1]):
    signs.append('-')
for i in range(info[2]):
    signs.append('*')
for i in range(info[3]):
    signs.append('/')

max_result = -1000000000
min_result = 1000000000
sign_list = list(set(permutations(signs, N-1)))
for i in range(len(sign_list)):
    calculate(sign_list[i])

print(max_result)
print(min_result)