import sys
sys.stdin = open('input.txt')

def test():
    for char in string:
        if char in parentheses:
            if char == '(' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return 0
                recent = stack.pop()
                if recent + char != '{}' and recent + char != '()':
                    return 0
    if len(stack) != 0:
        return 0
    return 1

T = int(input())
for tc in range(T):
    string = input()
    parentheses = ['(', ')', '{', '}']
    stack = []

    result = test()
    print("#{} {}".format(tc+1, result))