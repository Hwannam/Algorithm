paper = int(input())

white_paper = [[0]*100 for _ in range(100)]
for _ in range(paper):
    x, y = map(int, input().split())

    x = x - 1
    y = y - 1
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if white_paper[i][j] != 1:
                white_paper[i][j] = 1
print(sum(sum(white_paper, [])))
