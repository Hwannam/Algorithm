from collections import deque
import sys
N = int(sys.stdin.readline())
stack = deque()
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command[0:2] == 'pu':
        stack.append(command[5:])
    elif command[0:2] == 'to':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0:2] == 'si':
        print(len(stack))
    elif command[0:2] == 'em':
        if stack:
            print(0)
        else:
            print(1)
    else: # pop
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)