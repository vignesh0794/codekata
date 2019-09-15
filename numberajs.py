n=int(input())
a=str(n)
b=int(a[0:1])
c=int(a[1:2])
d=b+c
e=str(d)
f=(a[2:])
if(e in f):
	print("1")
else:
	print("0")
