import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    result = 1 if str1 in str2 else 0
    print("#{} {}".format(tc+1, result))