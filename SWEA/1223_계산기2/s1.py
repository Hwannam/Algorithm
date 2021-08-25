import sys
sys.stdin = open("input.txt")

for tc in range(10):
    length = int(input())
    string = input()
    stack = []
    new_string = ""
    for char in string:
        if char == '+' or char == '*':
            if ('+' in stack and char == '+') or ('*' in stack and char == '*') or ('*' in stack and char == '+'):
                new_string += stack.pop()
            stack.append(char)
        else:
            new_string += char
    while stack:
        new_string += stack.pop()

    stack.clear()
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