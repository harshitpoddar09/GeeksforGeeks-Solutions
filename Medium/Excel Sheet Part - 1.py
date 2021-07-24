class Solution:
    def ExcelColumn(self, N):
        #return required string
        #code here
        ans=''
        while N:
            a=N%26
            if a!=0:
                ans=chr(a-1+ord('A'))+ans
                N=N//26
            else:
                ans='Z'+ans
                N=(N//26)-1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends