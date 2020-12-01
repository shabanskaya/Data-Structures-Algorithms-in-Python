def dfs(a, j) :
	s = []
	ind = [0]*len(a)
	s.append( (j, a[j]) )
	i = 1
	while len(s)>0:
		if ind[s[-1][0]] == 0:
			ind[s[-1][0]] = i
			i += 1
			for e in s[-1][1] :
				s.append((e, a[e]))
		else:
			s.pop()

	return ind

n = int(input())
m = int(input())
a = [[] for i in range(n)]
b = [[] for i in range(n)]

for i in range(m):
	x, y = list(map(int, input().split()))
	a[x].append(y)
	b[y].append(x)

indb = dfs(b, 0)
	
for l in a:
	l.sort(key = lambda x : b[x])

j = indb.index(min(indb))
inda = dfs(a, j)
	
if max(inda) == len(a):
	print('YES')
else :
	print('NO')
