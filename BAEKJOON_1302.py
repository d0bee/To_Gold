N = int(input())
data = []

for _ in range(N):
    data.append(input())
data.sort()

data_set = list(set(data))
data_set.sort()
data_max = 0
result = ""
for i,j in enumerate(data_set):
    if data_max<data.count(j):
        data_max = data.count(j)
        result = j

print(result)