import sys

def check(num, direction):
    visited.append(num)
    temp_left = False
    temp_right = False
    if 0<= (num-1) and (num-1) not in visited:
        if state[num-1][2] != state[num][6]:
            temp_left = True
    if 3 >= (num+1) and (num+1) not in visited:
        if state[num][2] != state[num+1][6]:
            temp_right = True
    rotate(num, direction)
    if temp_left == True:
        check(num-1,-direction)
    if temp_right == True:
        check(num+1,-direction)

def rotate(num, direction):
    if direction == 1:
        temp = state[num][:7]
        temp = state[num][7] + temp
        state[num] = temp
    else:
        temp = state[num][1:]
        temp = temp + state[num][0]
        state[num] = temp

state = [str(sys.stdin.readline().strip()) for _ in range(4)]
K =int(sys.stdin.readline().strip())
method = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

for info in method:
    visited = []
    check(info[0]-1, info[1])

result = 0
if state[0][0] == '1':
    result += 1
if state[1][0] == '1':
    result += 2
if state[2][0] == '1':
    result += 4
if state[3][0] == '1':
    result += 8
print(result)