import sys
sys.stdin = open("input.txt")

def find_palindrome(N, M, string, result):
    for k in range(N - M + 1):
        if string[k:k + M] == string[k:k + M][::-1]:
            return len(string[k:k + M])
    return result

for _ in range(10):
    tc = int(input())
    chars = []
    result = 0
    for _ in range(100):
        chars.append(input())
    for i in range(100): # 가로
        for M in range(100, -1, -1):
            if result >= M:
                break
            result = find_palindrome(100, M, chars[i], result)

    for i in range(100): # 세로
        col_word = ""
        for j in range(100):
            col_word += chars[j][i]
        for M in range(100, -1, -1):
            if result >= M:
                break
            result = find_palindrome(100, M, col_word, result)

    print("#{} {}".format(tc, result))