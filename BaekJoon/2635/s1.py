T = int(input())
max_arr = [T]

for num in range(T, 0, -1):
    previous = T
    current_arr = [T]
    current_arr.append(num)
    while previous - num >= 0:
        current_arr.append(previous - num)
        previous, num = num, previous - num

    if len(current_arr) > len(max_arr):
        max_arr = current_arr

print(len(max_arr))
print(*max_arr)