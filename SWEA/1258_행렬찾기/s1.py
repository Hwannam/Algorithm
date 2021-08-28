import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    case = []
    for i in range(n):
        col = 0
        row = 1
        for j in range(n):
            if arr[i][j] != 0:
                arr[i][j] = 0
                col += 1
                for k in range(i+1, n):
                    if arr[k][j] != 0:
                        arr[k][j] = 0
                        if col == 1:
                            row += 1
                    else:
                        break
            elif arr[i][j] == 0 and col != 0:
                case.append([row, col])
                row = 1
                col = 0
    print("#{} {}".format(tc+1, len(case)), end = " ")
    while case:
        min_mul = 0
        for i in range(1, len(case)):
            if case[min_mul][0] * case[min_mul][1] > case[i][0] * case[i][1]:
                min_mul = i
            elif case[min_mul][0] * case[min_mul][1] == case[i][0] * case[i][1]:
                if case[min_mul][0] > case[i][0]:
                    min_mul = i
        print(case[min_mul][0], case[min_mul][1], end = " ")
        case.pop(min_mul)
    print()