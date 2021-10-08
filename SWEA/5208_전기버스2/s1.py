import sys
sys.stdin = open('input.txt')

def dfs(start):
    global count, result
    if count-1 >= result:
        return
    if start >= N-1:
        result = min(result, count-1)
        return
    for i in range(1,battery[start]+1):
        count += 1
        dfs(start+i)
        count -= 1

T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    N = arr[0]
    count = 0
    result = 10000000
    battery = list(arr[1:])
    dfs(0)
    print('#{} {}'.format(tc+1, result))