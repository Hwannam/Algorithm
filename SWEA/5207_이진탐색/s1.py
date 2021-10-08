import sys
sys.stdin = open('input.txt')

def binary_search(arr, target):
    global count
    left = 0
    right = len(arr) - 1
    side = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            count += 1
            return
        elif arr[mid] > target:
            right = mid - 1
            if side == -1:
                break
            side = -1
        elif arr[mid] < target:
            left = mid + 1
            if side == 1:
                break
            side = 1
    return

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    count = 0
    arr_A = sorted(list(map(int, input().split())))
    arr_B = list(map(int, input().split()))
    for number in arr_B:
        binary_search(arr_A, number)
    print('#{} {}'.format(tc+1, count))