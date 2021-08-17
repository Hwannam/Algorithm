import sys
sys.stdin = open("input.txt")

def find_palindrome(N, M, string):
    for k in range(N - M + 1):
        if string[k:k + M] == string[k:k + M][::-1]:
            return string[k:k + M]
    return False

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    chars = []
    result = 0
    for _ in range(N):
        chars.append(input())
    for i in range(N):
        result = find_palindrome(N, M, chars[i])
        if result != False:
            break

    if result == False:
        for i in range(N):
            col_word = ""
            for j in range(N):
                col_word += chars[j][i]
            result = find_palindrome(N, M, col_word)
            if result != False:
                break

    print("#{} {}".format(tc+1, result))