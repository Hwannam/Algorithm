import sys

def check_row(y,x):
    global answer
    previous = mat[y][x]
    i = 1
    visited = []
    result = True
    while i < N and result:
        if mat[y][x+i] == previous:
            pass
        elif mat[y][x+i] > previous:
                for j in range(1,L+1):
                    if mat[y][x+i] -1 == mat[y][x+i-j] and x+i-j not in visited:
                        visited.append(x+i-j)
                    else:
                        result = False
                        break
        elif mat[y][x+i] < previous:
                for j in range(L):
                    if previous -1 == mat[y][x+i+j] and x+i+j not in visited:
                        visited.append(x+i+j)
                    else:
                        result = False
                        break
        i+=1
    if result:
        answer +=1

def check_col(y,x):
    previous = mat[y][x]
    i = 1
    visited = []
    result = True
    while i < N and result:
        if mat[y+i][x] == previous:
            pass
        elif mat[y+i][x] > previous:
                for j in range(1,L+1):
                    if mat[y+i][x] -1 == mat[y+i-j][x] and y+i-j not in visited:
                        visited.append(y+i-j)
                    else:
                        result = False
                        break
        elif mat[y+i][x] < previous:
                for j in range(L):
                    if previous -1 == mat[y+i+j][x] and y+i+j not in visited:
                        visited.append(y+i+j)
                    else:
                        result = False
                        break
        i+=1
    if result:
        answer += 1

N, L = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
for i in range(N):
    check_row(i,0)
    check_col(0,i)
print(answer)
