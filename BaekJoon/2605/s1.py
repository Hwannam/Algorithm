student_num = int(input())
numbers = list(map(int, input().split()))

order = []
final_idx = -1
for student in range(student_num):
    final_idx += 1
    order.insert(final_idx - numbers[student], student + 1)
for item in order:
    print(item, end = " ")
