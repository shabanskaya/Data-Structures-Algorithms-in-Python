def sift_down(heap,i, n):
    while i * 2 +1 < n:
        j = i
        if heap[i] < heap[i*2 +1]:
            j = i*2 + 1
        if i * 2 + 2 < n and heap[j] < heap[i * 2 + 2]:
            j = i*2 +2
        if i == j:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j

from math import ceil

def build(heap, n):
    for i in range(ceil((len(heap))/2), -1, -1):
        sift_down(heap, i, n)
        
def heapsort(A):
    build(A, len(A))
    print(*A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        build(A, i)
        print(*A)
