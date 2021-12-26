def isPrime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0:
        return False
    for i in range(3,n,2):
        if n%i==0:
            return False
    return True
    
left,right=str(input()).split(',')
left=int(left)
right=int(right)
for i in range(left,right+1):
    if isPrime(i)==False:
        print(i,end=' ')