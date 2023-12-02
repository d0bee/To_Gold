T = int(input())

for _ in range(T):
    # 종점 = N, 최대 이동 수 = K, 충전기 수 = M
    # 최소 몇 번의 충전으로 종점에 도달할 수 있는지
    K, N, M = map(int, input().split())
    M_list = list(map(int,input().split()))

    # charge list
    C_list = [0] * N
    for i in M_list:
        C_list[i] = 1

    fuel = K
    now = 0
    cnt = 0
    width = [0] * N

    while now < N:
        if (C_list[now]) == 1 and (1 not in C_list[now+1:now+fuel+1] and now+fuel < N):
            fuel = K
            cnt += 1
        
        if fuel>0:
            width[now] = 1
            now += 1
            fuel -= 1
        else:
            cnt = 0
            break
        
    print(cnt)