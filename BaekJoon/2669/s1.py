import sys
sys.stdin = open("input.txt")

all = [[0]*100 for _ in range(100)]
for _ in range(4):
    input_square = list(map(int, input().split()))
    for i in range(input_square[0], input_square[2]):
        for j in range(input_square[1], input_square[3]):
            if all[j][i] == 0:
                all[j][i] = 1

print(sum(sum(all, [])))