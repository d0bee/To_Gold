N = int(input())
data = 0
for i in range(N):
    S = str(i)
    temp_sum = 0
    for j in range(len(S)):
        temp_sum += int(S[j])
    if (i+temp_sum) == N:
        data = i
        break
print(data)