n,k = map(int, input().split())

count = 0
while n!=1:
    
    if(n%k ==0):
        n = n//k
    else:
        n -=1
    count +=1
   
    if(n<k): #더이상 k로 나눌수 없을때 -1은 효율 bad
        break
count += (n-1)

print(count)
