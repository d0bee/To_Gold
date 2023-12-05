N = int(input())
data = []
data_f = []

for _ in range(N):
    data.append(input())
    data_f.append(data[_][0])

result = []
for i in range(N):
    if data_f.count(data_f[i]) >= 5:
        result.append(data_f[i])
result = list(set(result))
result.sort()

if len(result) == 0:
    print("PREDAJA")
else:
    print(''.join(result))