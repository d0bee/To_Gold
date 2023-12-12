T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    data = []
    for _ in range(N):
        data.append(input())
    
    result = ""

    # 가로 회문 찾기
    for i in range(N):
        for j in range(N - M + 1):
            if data[i][j:j+M] == data[i][j:j+M][::-1]:
                result = data[i][j:j+M]
                break
        if result:
            break

    # 세로 회문 찾기
    if not result:
        for i in range(N):
            column = ""
            for j in range(N):
                column += data[j][i]
            for k in range(N - M + 1):
                if column[k:k+M] == column[k:k+M][::-1]:
                    result = column[k:k+M]
                    break
            if result:
                break

    print(f"#{test_case} {result}")