import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
B,C = map(int, sys.stdin.readline().split())

result = 0
for place in A:
    result += 1
    place -= B
    if place > 0:
        if place%C == 0:
            result += place // C
        else:
            result += place // C + 1
print(result)