import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    string = []
    max_length = 0
    for _ in range(5):
        chars = input()
        if max_length < len(chars):
            max_length = len(chars)
        string.append(chars)
    result = ""
    for i in range(max_length):
        for j in range(5):
            if i >= len(string[j]):
                pass
            else:
                result += string[j][i]
    print("#{} {}".format(tc + 1, result))
