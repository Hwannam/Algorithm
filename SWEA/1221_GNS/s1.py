import sys
sys.stdin = open("input.txt")

# sort 내장함수 사용
T = int(input())
for _ in range(T):
    test_num, tc = input().split()
    tc = int(tc)
    numbers = input().split()
    earth_num = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

    for i in range(tc):
        numbers[i] = earth_num[numbers[i]]
    numbers.sort()
    for i in range(tc):
        for key, value in earth_num.items():
            if numbers[i] == value:
                numbers[i] = key
                break

    print("{} {}".format(test_num, ' '.join(numbers)))

