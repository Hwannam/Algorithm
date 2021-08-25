import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    rotation = []
    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(arr[j][i])
        rotation.append(temp)

    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(rotation[j][i])
        rotation.append(temp)

    for i in range(N):
        temp = []
        for j in range(2*N-1, N-1, -1):
            temp.append(rotation[j][i])
        rotation.append(temp)
    print("#{}".format(tc+1))
    for k in range(N):
        for i in range(k, 2*N+k+1, N):
            print("".join(map(str, rotation[i])), end = " ")
        print()