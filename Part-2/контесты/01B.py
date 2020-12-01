def dot_product(N, vector1, vector2):
    x = 0
    for i in range(N):
        x += vector1[i]*vector2[i]
    return x

