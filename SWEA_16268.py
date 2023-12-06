T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = [[0] * M for _ in range(N)]

    for i in range(N):
        data[i] = list(map(int, input().split()))
    
    