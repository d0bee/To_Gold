
T = int(input())
for _ in range(T):
    K = int(input())
    S = []
    Found = 0
    for i in range(K):
        S.append(input())

    A = ""
    B = ""
    for i in range(K):
        for j in range(K):
            if Found == 0 and i!=j:
                A = S[i]
                B = S[j]
                if A+B == (A+B)[::-1]:
                    Found = 1
                    break
        if Found == 1:
            break
    
    if Found == 1:
        print(A+B)
    else:
        print(0)
    