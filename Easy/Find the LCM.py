a,b=str(input()).split(',')
a=int(a)
b=int(b)
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print((a*b)//i)
        break