import sys
sys.stdin = open('input.txt')

code_info = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4', '0110001':'5', '0101111':'6',
             '0111011':'7', '0110111':'8', '0001011':'9'}

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = ''
    result = 0
    for row in arr:
        if row.count('0') != M: # 모두 0인줄은 거른다.
            for i in range(M-1, -1, -1): # 뒤에서부터 0이 아닐때
                if row[i] != '0':
                    code = row[i-55:i+1] # 56자리
                    break

    code_convert = ''
    for i in range(0,56,7): # 7자리씩 끊어서
        code_convert += code_info[code[i:i+7]]

    for i in range(0,7,2):
        result += int(code_convert[i])
    result *= 3
    for i in range(1,7,2):
        result += int(code_convert[i])
    result += int(code_convert[-1])

    answer = 0
    if result % 10 == 0:
        for num in code_convert:
            answer += int(num)
    print('#{} {}'.format(tc+1, answer))