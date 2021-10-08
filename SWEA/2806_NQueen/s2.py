import sys
sys.stdin = open("input.txt")

import copy
def find_case(arr, row, visit):
    global result
    global N

    for i in range(N):
        temp = copy.deepcopy(arr)
        temp_visit = list(visit)
        if temp[row][i] == 0 and temp_visit[i] == 0:
            if row == N - 1:
                result += 1
            else:
                temp[row][i] = 1
                temp_visit[i] = 1
                x = i
                y = row
                while 0<= x <=N-1 and 0<=y <=N-1:
                    if x != i and y != row:
                        temp[y][x] = 2
                    x -= 1
                    y -= 1

                x = i
                y = row
                while 0<= x <=N-1 and 0<=y <=N-1:
                    if x != i and y != row:
                        temp[y][x] = 2
                    x += 1
                    y += 1

                x = i
                y = row
                while 0<= x <=N-1 and 0<=y <=N-1:
                    if x != i and y != row:
                        temp[y][x] = 2
                    x -= 1
                    y += 1

                x = i
                y = row
                while 0<= x <=N-1 and 0<=y <=N-1:
                    if x != i and y != row:
                        temp[y][x] = 2
                    x += 1
                    y -= 1

                find_case(temp, row+1, temp_visit)
    return

T = int(input())
for tc in range(T):
    N = int(input())
    chess = [[0]*N for _ in range(N)]

    result = 0
    visited = [0]*N
    find_case(chess, 0, visited)
    print("#{} {}".format(tc+1, result))