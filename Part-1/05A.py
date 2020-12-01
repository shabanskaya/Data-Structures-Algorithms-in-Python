def cycle_shift(arr, N):
    a = arr[0]
    for i in range(N-1):
        arr[i] = arr[i+1]
    arr[N-1] = a
    return arr

#arr = [12, 3, 45, 6, 7]
#print(cycle_shift(arr, len(arr)))