import sys
sys.stdin = open('input.txt')

# 일일히 각 건물의 각 층마다 체크하는 방법
for T in range(1,11):
    buildings = int(input())
    list1 = list(map(int, input().split()))
    result = 0

    for i in range(2, buildings-2):
        for j in range(list1[i], 0, -1):
            if j > list1[i-2] and j > list1[i-1] and j > list1[i+1] and j > list1[i+2]:
                result += 1
            else:
                break
    print('#{} {}'.format(T, result))