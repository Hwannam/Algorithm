import sys
sys.stdin = open('input.txt')

code_info = {'1101':'0', '11001':'1', '10011':'2', '111101':'3', '100011':'4', '110001':'5', '101111':'6',
             '111011':'7', '110111':'8', '1011':'9'}

def find_gcd(a,b,c):
    for i in range(min(a,b,c), 0 ,-1):
        if a%i ==0 and b%i == 0 and c%i==0:
            return i

T = int(input())
for tc in range(20):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr = set(arr)
    arr = list(arr)
    codes = []
    final_codes = []
    answer = 0
    for row in arr: # 0인 행 및 좌우 0 제거 and 2진수 변환
        temp = ''
        if row.count('0') != M:
            for i in range(M):
                temp += bin(int(row[i], 16))[2:].rjust(4, '0')
            temp = temp.strip('0')
            codes.append(temp)

    for code in codes: # 코드 뽑아내기 2차
        temp = ''
        final_code = ''
        count = 0
        for i in range(len(code)-1, -1, -1): # 거꾸로 탐색
            if code[i] == '0' and code[i+1] == '1': # 1에서 0으로 바뀐 경우
                count += 1
            elif code[i] == '0' and len(temp) == 0: # 코드 사이에 0이 있는 경우 넘어감
                continue
            if count == 2: # 1 0 1 까지 나온 경우
                if temp not in code_info: # 배수인 경우 줄여주기
                    multiple = find_gcd(temp.index('0'), temp.count('0'), temp.count('1')-temp.index('0'))
                    temp_temp = ''
                    for j in range(0,len(temp), multiple):
                        temp_temp += temp[j]
                    temp = temp_temp
                final_code = code_info[temp] + final_code # 코드를 해독한다.
                temp = '' # 2진수를 담을 temp를 비워준다.
                count = 0
            else: # count가 2가 되기 전까지는 temp에 추가
                temp = code[i] + temp
            if len(final_code) == 8: # 해독한 코드가 8자리가 되면(한 행에 여러 코드가 있을 경우를 위해)
                if final_code not in final_codes: # 리스트에 없을때 추가 해준다.
                    final_codes.append(final_code)
                final_code = ''

        if temp != '': # 첫 열부터 숫자가 있는 경우, 위 루프에서 final code에 추가 못해줌
            if temp not in code_info:
                multiple = find_gcd(temp.index('0'), temp.count('0'), temp.count('1')-temp.index('0'))
                temp_temp = ''
                for j in range(0, len(temp), multiple):
                    temp_temp += temp[j]
                temp = temp_temp

            final_code = code_info[temp] + final_code
            if final_code not in final_codes:
                final_codes.append(final_code)

    for final_code in final_codes: # 바꾼 코드에 대해 처리
        result = (int(final_code[0]) + int(final_code[2]) + int(final_code[4]) + int(final_code[6]))*3 \
                 + int(final_code[1]) + int(final_code[3]) + int(final_code[5]) + int(final_code[7])

        if result % 10 == 0:
            for num in final_code:
                answer += int(num)
    print('#{} {}'.format(tc+1, answer))