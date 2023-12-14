T = int(input())
# 상 오 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
d = 0

for _ in range(T):
    N, M = map(int,input().split())

    data = [[0] * M for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    
    max_list = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            max_list[i][j] += data[i][j]
            
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if nr >= N or nr < 0  or nc >= M or nc < 0:
                    d += 1
                    continue
                else:
                    max_list[i][j] += data[nr][nc]
                    d += 1
    for i in max_list:
        print(i)
