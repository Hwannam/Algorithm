switch = int(input())
status = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    boygirl, number = map(int, input().split())
    if boygirl == 1:
        for idx in range(number-1, switch):
            if (idx + 1) % number == 0:
                status[idx] = (status[idx] + 1) % 2
    else:
        plus = 0
        idx = number - 1
        while True:
            if idx - plus - 1 < 0 or idx + plus + 1 >= switch:
                break
            plus += 1
            if status[idx + plus] != status[idx - plus]:
                plus -= 1
                break
        for plus in range(0, plus+1):
            status[idx + plus] = (status[idx + plus] + 1) % 2
            if plus != 0:
                status[idx - plus] = (status[idx - plus] + 1) % 2
for i in range(switch):
    if i != 0 and i % 20 == 0:
        print()
    print(status[i], end = " ")