#User function Template for python3

class Solution:
 
    #Function to add two matrices.
    def sumMatrix(self,A,B):
        # code here
        if len(A)!=len(B) or len(A[0])!=len(B[0]):
            return []
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col]+=B[row][col]
        return A


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1,m1 = map(int,input().strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                A[i][j]=line1[k]
                k+=1
       
        n2,m2 = map(int,input().strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n2):
            for j in range (m2):
                B[i][j]=line2[k]
                k+=1
        
        obj = Solution()
        ans = obj.sumMatrix(A,B)
        if(len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range (len(ans[0])):
                    print(ans[i][j],end=' ')
            print() 

# } Driver Code Ends