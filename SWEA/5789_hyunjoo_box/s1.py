import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    result = [0 for _ in range(N)]     # 상자에 숫자가 처음에 모두 0으로

    for i in range(1, Q+1):            # Q번 작업한다.
        L, R = map(int, input().split())
        for index in range(L-1, R):    # L부터 R까지를 i로 변경
            result[index] = i
    print("#{}".format(tc + 1), end = " ")
    for item in result:                # 리스트 요소 출력
        print(item, end = " ")
    print()