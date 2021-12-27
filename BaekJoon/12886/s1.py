import sys
from collections import deque, defaultdict

def bfs(first):
    global result
    queue = deque()
    queue.append(first)
    visited = defaultdict(bool)
    visited[first] = True
    while queue:
        temp = queue.popleft()
        if temp[0]==temp[1]==temp[2]:
            result = 1
            break
        for i in range(2):
            for j in range(i+1,3):
                if temp[i] != temp[j]:
                    if temp[i] < temp[j]:
                        new_mat = (temp[i]*2, temp[j]-temp[i], sum_all-temp[i]-temp[j])
                    elif temp[i] > temp[j]:
                        new_mat = (temp[j] * 2, temp[i] - temp[j], sum_all - temp[i] - temp[j])
                    if visited[new_mat] == False:
                        queue.append(new_mat)
                        visited[new_mat] = True

mat = list(map(int, sys.stdin.readline().split()))
sum_all = sum(mat)
result = 0
if sum(mat) % 3 == 0:
    bfs((mat[0],mat[1],mat[2]))
print(result)