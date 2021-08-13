N, K = map(int, input().split())
girl = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
boy = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        boy[Y] += 1
    else:
        girl[Y] += 1

room = 0
for value in girl.values():
    room += value // K if value % K == 0 else value // K + 1
for value in boy.values():
    room += value // K if value % K == 0 else value // K + 1
print(room)