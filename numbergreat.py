n=int(input())

def getSum(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
def getProduct(n): 
    product = 1
    while (n != 0): 
        product = product * (n % 10) 
        n = n // 10
    return product 
d=getSum(n)
e=getProduct(n)
f=d+e
if(f==n):
    print("Great")
else:
    print("no")
