class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,arr,N):
        #Your code here
        i=0
        while i+1<N:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=2
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        ob=Solution()
        ob.convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends