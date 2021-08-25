import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    queue = list(map(int, input().split()))
    count = 0
    while True:
        add_num = queue.pop(0) - count - 1
        queue.append(add_num)
        if add_num <= 0:
            queue[-1] = 0
            break
        count = (count + 1) % 5
    print("#{} {}".format(tc, " ".join(map(str, queue))))