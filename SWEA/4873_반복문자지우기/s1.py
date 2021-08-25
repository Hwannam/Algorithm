import sys
sys.stdin = open('input.txt')

def erase_repeat():
    for char in string:
        if len(stack) != 0:
            recent = stack.pop()
            if recent != char:
                stack.append(recent)
            else:
                continue
        stack.append(char)
    return len(stack)

T = int(input())
for tc in range(T):
    string = input()
    stack = []
    print("#{} {}".format(tc+1, erase_repeat()))