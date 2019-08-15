n=int(input("enter the number:"))
sum=0
tmp=n
while tmp>0:
    digit=tmp%10
    sum+=digit**3
    tmp//=10
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")