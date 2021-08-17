import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    answer = 1
    sort_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sort_num != sorted(puzzle[i]):
            answer = 0
            break
    if answer == 1:
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(puzzle[j][i])
            if sort_num != sorted(temp):
                answer = 0
                break
    if answer == 1:
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                temp = []
                for i in range(3):
                    temp.extend(puzzle[x+i][y:y+3])
                if sort_num != sorted(temp):
                    answer = 0
                    break

    print("#{} {}".format(tc+1, answer))