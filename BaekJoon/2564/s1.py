row, col = map(int, input().split())
store = int(input())

location = []
for count in range(store + 1):
    direction, distance = map(int, input().split())
    if direction == 1:
        location.append((distance, 0))
    elif direction == 2:
        location.append((distance, col))
    elif direction == 3:
        location.append((0, distance))
    else:
        location.append((row, distance))

result = 0
x, y = location.pop()

for coordinate in location:
    if coordinate[1] == y:
        result += abs(x - coordinate[0])

    elif abs(coordinate[1] - y) == col:
        x_sum = x + coordinate[0]
        result += (col + min(x_sum, 2*row - x_sum))
    else:
        result += (abs(x - coordinate[0]) + abs(y - coordinate[1]))
print(result)