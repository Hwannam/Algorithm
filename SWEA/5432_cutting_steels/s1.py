import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    parentheses = input()
    stack = result = 0
    previous = ""
    for char in parentheses:
        if char == '(':   # stack에 ( 만 push 한다.
            stack += 1
        else:
            if previous == '(':     # 레이저가 완성된 경우
                stack -= 1
                result += stack     # 그 전까지의 막대기를 잘라서 더한다.
            elif previous == ')':   # 막대기가 끝난 경우
                result += 1         # 막대기 조각 1개를 더해준다.
                stack -= 1
        previous = char
    print("#{} {}".format(tc+1, result))