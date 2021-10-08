import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, hexa_num = input().split()
    result = bin(int(hexa_num, 16))[2:]
    if len(result) % 4 != 0:
        add_zero = 4 - (len(result) % 4)
        result = '0'*add_zero + result
    print("#{} {}".format(tc+1, result))