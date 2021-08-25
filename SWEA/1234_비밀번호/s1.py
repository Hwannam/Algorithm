import sys
sys.stdin = open('input.txt')

for tc in range(10):
    total, numbers = input().split()
    stack = []
    for number in numbers:
        if not stack:
            stack.append(number)
        elif stack[-1] == number:
            stack.pop()
        else:
            stack.append(number)

    print("#{} {}".format(tc+1, "".join(stack)))