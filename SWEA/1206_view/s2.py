import sys
sys.stdin = open('input.txt')


# 건물의 층수를 빼는 방법
for T in range(1,11):
    buildings = int(input())
    list1 = list(map(int, input().split()))
    result = 0
    for i in range(2, buildings-2):
        if max(list1[i - 2], list1[i - 1], list1[i + 1], list1[i + 2]) < list1[i]:
            result += (list1[i] - max(list1[i - 2], list1[i - 1], list1[i + 1], list1[i + 2]))

    print('#{} {}'.format(T, result))