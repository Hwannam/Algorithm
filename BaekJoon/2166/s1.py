import sys

while True:
    case = sys.stdin.readline().strip()
    if case == 'end':
        break
    xcnt = case.count('X')
    ocnt = case.count('O')

    if ocnt + 1 != xcnt or (xcnt < 3 and ocnt < 3):
        print('invalid')
        continue
    else:

