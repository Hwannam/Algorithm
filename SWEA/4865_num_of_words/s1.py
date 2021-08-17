import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    max_count = 0
    for i in range(len(str1)):
        max_count = max(max_count, str2.count(str1[i]))
    print("#{} {}".format(tc + 1, max_count))