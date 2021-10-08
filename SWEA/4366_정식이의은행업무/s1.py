import sys
sys.stdin = open('input.txt')

def find_binary(num):
    index = 0
    while index < len(num):
        temp = ''
        for i in range(len(num)):
            if index == i:
                if num[i] == '0':
                    temp += '1'
                else:
                    temp += '0'
                temp += num[i+1:]
                binary_list.append(int(temp, 2))
                break
            else:
                temp += num[i]
        index += 1

def find_ternary(num):
    index = 0
    while index < len(num):
        temp = ''
        for i in range(len(num)):
            if index == i:
                if num[i] == '0':
                    temp1 = temp + '1' + num[i+1:]
                    temp2 = temp + '2' + num[i + 1:]
                elif num[i] == '1':
                    temp1 = temp + '0' + num[i + 1:]
                    temp2 = temp + '2' + num[i + 1:]
                else:
                    temp1 = temp + '0' + num[i + 1:]
                    temp2 = temp + '1' + num[i + 1:]
                if int(temp1, 3) in binary_list:
                    return int(temp1, 3)
                elif int(temp2, 3) in binary_list:
                    return int(temp2, 3)
                break
            else:
                temp += num[i]
        index += 1

T = int(input())
for tc in range(T):
    binary = input()
    ternary = input()
    binary_list = []
    find_binary(binary)
    print('#{} {}'.format(tc+1, find_ternary(ternary)))