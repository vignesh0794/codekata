n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(0,n):
	if((l[i]%k)==0):
	    print("1")
	else:
	    print("0",end=" ")
