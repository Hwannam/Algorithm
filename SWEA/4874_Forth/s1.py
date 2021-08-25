import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    code = list(input().split())
    stack = []
    calculate = ['+', '-', '*', '/']
    for char in code:
        if char not in calculate: # 숫자 or .
            if char == '.':
                if len(stack) == 1:
                    print("#{} {}".format(tc+1, int(stack.pop())))
                else:
                    print("#{} error".format(tc + 1))
            else: # 숫자
                stack.append(char)
        else:
            if len(stack) >= 2:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num2 - num1)
                elif char == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(num2 / num1)
            else:
                print("#{} error".format(tc + 1))
                break # 마지막이 아닌데 오류이므로