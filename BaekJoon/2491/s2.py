N = int(input())

number = list(map(int, input().split()))
length = max_length = 1

for i in range(N - 1):
    if number[i] <= number[i+1]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
    if i+1 == len(number) - 1:
        max_length = max(max_length, length)
        length = 1

for i in range(N - 1):
    if number[i] >= number[i+1]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
    if i+1 == len(number) - 1:
        max_length = max(max_length, length)

print(max_length)
