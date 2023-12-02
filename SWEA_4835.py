T = int(input())
T_list = [0] * T

for _ in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    max_min = [0] * (len(N_list)-M+1) 
    for i in range(len(max_min)):
        max_min[i] = sum(N_list[i:i+M])
    T_list[_] = max(max_min)-min(max_min)

for i,num in enumerate(T_list):
    print("#",i+1,num)