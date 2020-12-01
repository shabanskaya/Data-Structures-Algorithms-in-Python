def largest_rect(N, array):
    s = []
    for i in range(N):
        c = 0
        for ii in range (i, -1, -1):
            if array[ii] >= array[i]:
                c += array[i]
            else:
                break
        for ii in range (i+1, N):
            if array[ii] >= array[i]:
                c += array[i]
            else:
                break
        s.append(c)
    return (max(s))
