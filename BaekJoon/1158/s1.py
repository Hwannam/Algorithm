N, index = map(int, input().split())
numbers = list(i for i in range(1, N+1))
result = []
current = index - 1
while True:
    result.append(numbers[current])
    numbers.pop(current)
    if len(numbers) == 0:
        break
    current = (current + index - 1) % len(numbers)
print("<", end = '')
for i in range(N):
    print(result[i], end = '')
    if i == N-1:
        print('>')
    else:
        print(", ", end = '')