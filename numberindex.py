n,k=map(int,input().split())
l=list(map(int,input().split()))

if(k in l ):
	index = l.index(k)
	print(index)
else:
	print("-1")
