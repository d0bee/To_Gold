a = [0] * 9
for i in range(len(a)):
    a[i] = int(input())
a.sort()

num = sum(a)-100
data = []
cnt = 0
for i in range(len(a)-1):
    for j in range(len(a)):
        if a[i] + a[j] == num and cnt == 0:
            data.append(a[i])
            data.append(a[j])
            cnt += 1

for i in a:
    if i not in data:
        print(i)