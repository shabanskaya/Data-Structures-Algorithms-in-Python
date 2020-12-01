def sift_up(heap,i):
    while i > 0 and heap[(i-1)//2] > heap[i]:
        heap[i],heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        i = (i-1)//2

def add(heap,x):
    heap.append(x)
    sift_up(heap,len(heap) - 1)

n = int(input())
a = list(map(int,input().split()))

heap = []
for e in a:
    add(heap,e)

print(*heap)