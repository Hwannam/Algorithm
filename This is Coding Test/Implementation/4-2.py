n = int(input())
time=0 
minute=0
sec =0
count = 0

while True:
    sec +=1
    if(sec == 60):
        sec = 0
        minute +=1
    if(minute == 60):
        minute =0
        time +=1 

    if('3' in str(time)+str(minute)+str(sec)): #문자열로 변환후 3찾기
        count +=1    

    if(time == n+1):
        break

print(count)