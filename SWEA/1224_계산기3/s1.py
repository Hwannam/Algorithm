import sys
sys.stdin = open("input.txt")

for tc in range(10):
    length = int(input())
    string = input()
    stack = []
    new_string = ""
    for char in string:
        if char == '+' or char == '*':
            if (stack[-1] == '+' and char == '+') or (stack[-1] == '*' and char == '*') or (stack[-1] == '*' and char == '+'):
                if stack[-1] != '(':
                    new_string += stack.pop()
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                new_string += temp
        else:
            new_string += char
    while stack:
        new_string += stack.pop()

    for char in new_string:
        if char == '+' or char == '*':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if char == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)
        else:
            stack.append(char)
    print("#{} {}".format(tc+1, stack.pop()))