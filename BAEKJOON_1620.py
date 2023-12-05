N,M = map(int, input().split())

data = {}
data_list = {}

for i in range(1,N+1):
    S = input()
    data[i] = S
    data_list[S] = i

for _ in range(M):
    select = input()

    if select.isdigit():
        print(data[int(select)])
    else:
        print(data_list[select])