location = input()
col = ord(location[0]) - ord('a') + 1
row = int(location[1])
count = 0
move = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

for i in move:
    if(1<=row+i[1]<=8 and 1<=col+i[0]<=8):
        count +=1
print(count)