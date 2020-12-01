def bubble_sort2d(matrix, N, M):
    for k in range(N):
        print(*matrix[k])
    print()
    for _ in range(N*M):
        j = 0
        while j<N:
            for i in range(M-1):
                if matrix[j][i] > matrix[j][i+1]:
                    matrix[j][i], matrix[j][i+1] = matrix[j][i+1], matrix[j][i]
                    for k in range(N):
                        print(*matrix[k])
                    print()
            if j!=N-1:
                if matrix[j][M-1]> matrix[j+1][0]:
                    matrix[j][M-1], matrix[j+1][0] = matrix[j+1][0], matrix[j][M-1]
                    for k in range(N):
                        print(*matrix[k])
                    print()
            j+=1

                