def cycle_shift_M(arr, N, M):
    for i in range(M):
        x = arr.pop(0)
        arr.append(x)
