def trial(a, el, n) : #вопрос: есть ли в массиве a элемент el, n раз
	i = len(a)-1
	k = 0
	while i > -1 and k < 2:
		if a[i] == el :
			k += 1
		i -= 1
	
	if k >= n :
		return True 
	else :
		return False 


def dfs_circle(a, j, ind) : # a - массив, где индексу-номеру вершины соответствует список его потомков,
							# j - номер вершины-начала поиска, ind - массив индикаторов: 0 - не посещали, 1 - посещали 1 раз, 2 - более двух раз
	s = [[], [] ]
	s[0].append(j) # стек номеров вершин
	s[1].append(j) # соответствующие им вершины-прародители - откуда алгоритм пришел в эту вершину

	up = True # Индикатор направления движения - пришли мы в вершину сверху или снизу по стеку (удаляли мы вершину перед этим или наоборот добавляли)
	while s[0] :
		if ind[ s[0][-1] ] == 0  :
			ind[ s[0][-1] ] = 1
			t = s[0][-1] # времянка чтобы перенести во внутренний цикл номер вершины из которой попали в добавляемые
			if a[ s[0][-1] ] : # потомки текущего
				up = True
			else:
				up = False
			for el in  a[ s[0][-1] ] :
				s[0].append( el )
				s[1].append(t)
#				print(s[0], ind, 'el = ', el )
		elif ind[ s[0][-1] ] == 1 and up == True : # нашли цикл - пришли в вершину снизу, выйдя уже из неё однажды
#			print(s[0], ind)
			return s
		else :
			ind[ s[0][-1] ] = 2
			s[0].pop()
			s[1].pop()
			up = False
#			print(s[0], ind)
	return s


def main() :
	n, m  = input().split()
	n = int(n)
	m = int(m)
	a = [[] for i in range(n)]
	b = [[] for i in range(n)]
	ind = [0]*n

	i = 0	
	while i < m :
		s1, s2 = input().split()
		s1 = int(s1)
		s2 = int(s2)
		a[s1].append(s2)

		i += 1
#	print(a)

	s = dfs_circle(a, 0, ind)
#	print(s, ind)
	
	while (not s[0]) and trial(ind, 0, 1) : # пока поиск выдает пустой массив, то есть проведен до конца без циклов, и пока есть непройденные вершины
		i = 0
		while ind[i] != 0 and i < n : # Найти ноль индикатора (непосещенная вершина)
			i += 1
		s = dfs_circle(a, i, ind) # поиск в ней
#		print(s)

	if not s[0] :
		print('YES')
#	elif len(s[0]) <= 2 :
#		print(' '.join( map(str, s[0]) ) )
	else :
#		print(s[0], s[1])

		i = len(s[0])-1
		res = [ s[0][-1] ]
		x = s[1][-1]
		while i > -1 : # проход по стеку вниз в соответствии с массивом предков s[1] (идти вниз пока не найдешь нужного предка, если нужный предок - последний, то остановиться)
#			print(res, x, i)
			if s[0][i] == x :
				res.append( s[0][i] )
				x = s[1][i]
				if res[-1] == s[0][-1] and i < len(s[0])-1 :
#					print(res, "i, len(s[0])-1 = ", i, len(s[0])-1, s[0])
					break
			i -= 1
		if res[0] == res[-1] :
			res.pop(0)
		print(' '.join( map(str, reversed(res)) ) )
	

if __name__ == "__main__":
	main()
