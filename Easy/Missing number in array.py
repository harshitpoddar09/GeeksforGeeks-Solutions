class Solution:
    def MissingNumber(self,array,n):
        # code here
        if n not in array:
            return n
        array=sorted(array)
        for i in range(1,n):
            if array[i-1]!=i:
                return i

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends