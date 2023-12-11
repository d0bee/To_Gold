N = int(input())
data = []
max_n = 0
for _ in range(N):
    a, b = map(int, input().split())

    if max_n < b:
        max_n = b
    
    while len(data) < max_n:
        data.append(0)
    data.append(0)

    for i in range(a,b+1):
        
        data[i] = 1
print(data)