import sys

sys.stdin = open("input.txt")

# sort 함수 사용
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    mode = 0  # 큰수 작은수 반복
    result = []
    start = 0
    end = N - 1
    while len(result) < 10:  # 10개만 출력하면 되므로
        if mode == 0:  # 큰 수 찾기
            result.append(arr[end])
            end -= 1  # 가장 큰 수, 두번째 큰 수, 세번째 ...
        elif mode == 1:  # 작은 수 찾기
            result.append(arr[start])
            start += 1  # 가장 작은 수, 두번째 작은 수, 세번째 ...
        mode = (mode + 1) % 2  # 0 1 반복

    print("#{}".format(tc + 1), end=" ")
    for item in result:
        print(item, end=" ")
    print()