n = int(input()) 
arr=list(map(int,input().split()))
a=max(arr)
b=min(arr)
d=arr.index(a)
e=arr.index(b)
c=d-e
print(c)
