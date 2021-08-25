import sys
sys.stdin = open('input.txt')

for tc in range(10):
    total, num = input().split()
    numbers = []
    numbers.extend(num)
    idx = 0
    while True:
        if numbers[idx] == numbers[idx + 1]:
            del numbers[idx:idx+2]
            idx -= 1
        else:
            idx += 1
        if idx == len(numbers)-1:
            break
    print("#{} {}".format(tc+1, "".join(numbers)))