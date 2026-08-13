n=int(input("ener the number: "))
tem=n
sum=0
digits=len(str(n))

while tem>0:
    dig=tem%10
    sum=sum+dig**digits
    tem=tem//10

if sum==n:
    print(n,"is armstrong number")
else:
    print(n,"is not")