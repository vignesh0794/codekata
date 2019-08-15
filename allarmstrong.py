a=int(input("enter the starting number"))
b=int(input("enter the ending number"))
for num in range(a,b+1):
    sum=0
    tmp=num
    while tmp>0:
        digit=tmp%10
        sum+=digit**3
        tmp//=10
    if num==sum:
        print(num)