class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]>k:
                hi=mid-1
            else:
                lo=mid+1
        return -1

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends