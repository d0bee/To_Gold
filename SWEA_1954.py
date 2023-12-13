T = int(input())
for _ in range(T):
    N = int(input())
    data = [[0] * N for _ in range(N)]

    spin_r = [0,1,0,-1]
    spin_c = [1,0,-1,0]

    r, c, d = 0, 0, 0

    for i in range(1,N**2+1):
        data[r][c] = i

        nr, nc = r + spin_r[d], c + spin_c[d]

        if nr>=N or nr<0 or nc>=N or nc<0 or data[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + spin_r[d], c + spin_c[d]
        
        r, c = nr, nc

    print(f"#{_+1}")
    for i in data:
        print(*i)
    