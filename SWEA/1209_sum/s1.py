import sys
sys.stdin = open("input.txt")

for tc in range(10):
    case_num = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    max_row = max_col = sum_diag = sum_diag_reverse = 0

    for i in range(100):
        if sum(arr[i]) > max_row:   # row의 max를 찾는 코드
            max_row = sum(arr[i])

        sum_col = 0
        for j in range(100):        # col의 max를 찾는 코드
            sum_col += arr[j][i]
        if max_col < sum_col:
            max_col = sum_col

        sum_diag += arr[i][i]       # 대각선의 합을 구함
        sum_diag_reverse += arr[i][99-i]    # 역대각선의 합을 구함

    print("#{} {}".format(case_num, max(max_row, max_col, sum_diag, sum_diag_reverse)))