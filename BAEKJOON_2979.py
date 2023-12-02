A, B, C = map(int, input().split())
time = [0] * 100
sum = 0

for i in range(3):
    temp = list(map(int, input().split()))
    for j in range(temp[0],temp[1]):
        time[j] += 1
        
for i in time:
    if i == 1:
        sum += A
    elif i == 2:
        sum += B*2
    elif i == 3:
        sum += C*3

print(sum)