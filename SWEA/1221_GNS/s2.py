import sys
sys.stdin = open("input.txt")

# 빠른정렬 사용 -----------------> 빠르다.
def quick_sort(arr):
    earth_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        num_value = earth_num[num]
        pivot_value = earth_num[pivot]
        if num_value < pivot_value:
            lesser_arr.append(num)
        elif num_value > pivot_value:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

T = int(input())
for _ in range(T):
    test_num, tc = input().split()
    tc = int(tc)
    numbers = input().split()

    numbers = quick_sort(numbers)

    print("{} {}".format(test_num, ' '.join(numbers)))