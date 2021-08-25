import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    triangle = []
    for i in range(N):
        temp = [1]
        if i != 0:
            if i != 1:
                for j in range(i-1):
                    temp.append(triangle[i-1][j]+ triangle[i-1][j+1])
            temp.append(1)
        triangle.append(temp)
    print("#{}".format(tc+1))
    for row in triangle:
        print(" ".join(map(str, row)))