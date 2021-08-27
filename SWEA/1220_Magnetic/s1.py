import sys
sys.stdin = open("input.txt")

for tc in range(10):
    size = int(input())
    table = [list(input().split()) for _ in range(100)]
    result = 0
    for i in range(100):
        magnet = []
        for j in range(100):
            if table[j][i] != '0':
                magnet.append(table[j][i])
        for k in range(len(magnet)):
            if magnet[k] == '2':
                magnet[k] = '0'
            else:
                break
        for k in range(len(magnet)-1, -1, -1):
            if magnet[k] == '1':
                magnet[k] = '0'
            else:
                break
        magnet = "".join(magnet)
        result += magnet.count("12")
    print("#{} {}".format(tc+1, result))