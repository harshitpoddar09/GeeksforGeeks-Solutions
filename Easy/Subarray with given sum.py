#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        #Your code here
        w_start=0
        cur_sum=0
        for w_end in range(n):
            cur_sum+=arr[w_end]
            if cur_sum==s:
                return [w_start+1,w_end+1]
            while cur_sum>s:
                cur_sum-=arr[w_start]
                w_start+=1
            if cur_sum==s:
                return [w_start+1,w_end+1]
        return [-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends