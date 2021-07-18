n = int(input())
move =  list(input().split())

x= 1
y= 1

for i in move:
    if(i == 'L'):
        nx = x
        ny = y - 1
    elif(i == 'R'):
        nx = x
        ny = y +1
    elif(i == 'U'):
        nx = x-1
        ny = y
    elif(i == 'D'):
        nx = x+1
        ny = y
    
    if(1<= nx <=5 and 1<= ny <=5):
        x = nx
        y = ny
print(x, y)
    



