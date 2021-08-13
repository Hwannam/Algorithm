import sys
sys.stdin = open("input.txt")

# 선택정렬을 사용 -----------> 느리다...
T = int(input())
for _ in range(T):
    test_num, tc = input().split()
    tc = int(tc)
    numbers = input().split()
    earth_num = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

    for i in range(tc - 1): # 선택 정렬
        index_min = i
        for j in range(i + 1, tc):
            if earth_num[numbers[j]] < earth_num[numbers[index_min]]:
                index_min = j
        numbers[index_min], numbers[i] = numbers[i], numbers[index_min]

    print("{} {}".format(test_num, ' '.join(numbers)))