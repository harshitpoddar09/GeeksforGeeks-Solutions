def isPrime(n):
    # code here
    if n<=1:
        return 0
    elif n==2 or n==3:
        return 1
    elif n%2==0:
        return 0
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return 0
    return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.

if __name__ == '__main__': 
    n=int(input())
    print(isPrime(n))
# } Driver Code Ends