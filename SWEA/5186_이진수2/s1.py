import sys
sys.stdin = open('input.txt')

def to_bin(num):
    count = -1
    result = ''
    while num != 0:
        result += str(int(num // (2**count)))
        num %= 2**count
        count -= 1
        if len(result) >= 14:
            return 'overflow'
    return result

T = int(input())
for tc in range(T):
    N = float(input())
    answer = to_bin(N)
    print("#{} {}".format(tc+1, answer))