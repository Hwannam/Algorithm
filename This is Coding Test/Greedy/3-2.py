# 큰 수의 법칙-+
n, m, k = map(int, input().split())

data = list(map(int,input().split()))

data.sort() #오름차순
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m ==0:
            break
        result = result + first 
        m -=1 

    if(m==0):
        break
    result = result + second
    m -=1

# 시간 초과 안뜨는 방법
# count = int(m/(k+1)) *k
# count += m%(k+1)

# result = 0

# result += count *first
# result += (m-count) *second    

print(result)

