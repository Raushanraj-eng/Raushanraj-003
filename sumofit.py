n=int(input("enter the number: "))
m=0
while n>0:
    a=n%10
    print(a)
    m+=a
    n//=10
print("____________________________________________________________")
print(m)