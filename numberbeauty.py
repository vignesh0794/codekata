n=int(input())
l=list(map(int,input().split()))
a=sum(l)
if((a%2==0)&(a%3==0)&(a%5==0)):
	print("1")
else:
	print("0")
