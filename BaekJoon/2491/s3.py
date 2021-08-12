N = int(input())
num_list = list(map(int, input().split()))

max_cnt = 1
cnt_bigger = 1
cnt_lower = 1
for i in range(N-1):
    if num_list[i] < num_list[i+1]:
        max_cnt = max(max_cnt, cnt_lower)
        cnt_lower = 1
        cnt_bigger += 1
    elif num_list[i] > num_list[i+1]:
        max_cnt = max(max_cnt, cnt_bigger)
        cnt_bigger = 1
        cnt_lower += 1
    else:
        cnt_bigger += 1
        cnt_lower += 1

    max_cnt = max(max_cnt, max(cnt_bigger, cnt_lower))

print(max_cnt)