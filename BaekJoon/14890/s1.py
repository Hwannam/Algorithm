import sys

def check_row(y,x):
    global answer
    previous = mat[y][x]
    i = 1
    visited = []
    result = True
    while i < N and result:
        if x+i in visited:
            previous = mat[y][x+i]
            i+=1
            continue
        if mat[y][x+i] == previous:
            pass
        elif mat[y][x+i] > previous:
                if x+i-L < 0:
                    result = False
                    break
                for j in range(1,L+1):
                    if mat[y][x+i] -1 == mat[y][x+i-j] and x+i-j not in visited:
                        visited.append(x+i-j)
                    else:
                        result = False
                        break
                previous = mat[y][x + i]
        elif mat[y][x+i] < previous:
                if x+i+L-1 >= N:
                    result = False
                    break
                for j in range(L):
                    if previous -1 == mat[y][x+i+j] and x+i+j not in visited:
                        visited.append(x+i+j)
                    else:
                        result = False
                        break
                previous = mat[y][x + i]
        i+=1
    if result:
        answer +=1

def check_col(y,x):
    global answer
    previous = mat[y][x]
    i = 1
    visited = []
    result = True
    while i < N and result:
        if y+i in visited:
            previous = mat[y + i][x]
            i += 1
            continue
        if mat[y+i][x] == previous:
            pass
        elif mat[y+i][x] > previous:
                if y + i - L < 0:
                    result = False
                    break
                for j in range(1,L+1):
                    if mat[y+i][x] -1 == mat[y+i-j][x] and y+i-j not in visited:
                        visited.append(y+i-j)
                    else:
                        result = False
                        break
                previous = mat[y + i][x]
        elif mat[y+i][x] < previous:
                if y+i+L-1 >= N:
                    result = False
                    break
                for j in range(L):
                    if previous -1 == mat[y+i+j][x] and y+i+j not in visited:
                        visited.append(y+i+j)

                    else:
                        result = False
                        break
                previous = mat[y+i][x]
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